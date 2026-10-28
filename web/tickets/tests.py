import re

from django.test import TestCase


class TicketPageTests(TestCase):
    def test_landing_page_introduces_the_site_and_links_to_travel_modes(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How would you like to travel?")
        self.assertContains(response, "Compare routes, schedules, durations")
        for path in ("/flights/", "/trains/", "/ships/", "/hotels/"):
            with self.subTest(path=path):
                self.assertContains(response, f'href="{path}"')

    def test_shared_bootstrap_layout_is_used_across_pages(self):
        for path in ("/", "/flights/", "/trips/flight/1/"):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "bootstrap@5.3.3/dist/css/bootstrap.min.css")
                self.assertContains(response, 'class="navbar-toggler"')

    def test_category_pages_load(self):
        for path, title in (
            ("/flights/", "Flight Tickets"),
            ("/trains/", "Train Tickets"),
            ("/ships/", "Ship Tickets"),
            ("/hotels/", "Hotels"),
        ):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, title)
                self.assertContains(response, "Django runs the search")
                if path in ("/flights/", "/trains/", "/ships/"):
                    self.assertContains(response, 'value="duration"')
                    self.assertContains(response, 'value="departure"')

    def test_trip_detail_pages_show_trip_specific_information(self):
        cases = (
            ("/trips/flight/1/", "Garuda Indonesia / GA101", "Jakarta", "Surabaya"),
            ("/trips/train/1/", "Argo Bromo Anggrek / Train 1", "Jakarta", "Surabaya"),
            ("/trips/ship/1/", "PELNI / KM Gunung Dempo", "Jakarta", "Makassar"),
        )
        for path, provider_number, origin, destination in cases:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, provider_number)
                self.assertContains(response, origin)
                self.assertContains(response, destination)
                self.assertContains(response, "Journey duration")
                self.assertContains(response, "Ticket price")
                self.assertContains(response, f"<dd>{path.split('/')[2].title()}</dd>")
                self.assertNotContains(response, f"<dd>{path.split('/')[2].title()} tickets</dd>")

    def test_trip_detail_returns_not_found_for_unknown_trip(self):
        self.assertEqual(self.client.get("/trips/flight/999/").status_code, 404)
        self.assertEqual(self.client.get("/trips/hotel/1/").status_code, 404)


class TicketApiTests(TestCase):
    def test_sort_returns_flight_numbers_and_airport_codes(self):
        response = self.client.get("/api/tickets/", {"action": "sort"})

        self.assertEqual(response.status_code, 200)
        tickets = response.json()["tickets"]
        self.assertEqual(
            [ticket["price"] for ticket in tickets],
            sorted(ticket["price"] for ticket in tickets),
        )
        bali_flight = next(ticket for ticket in tickets if ticket["destination"] == "Bali")
        self.assertEqual(bali_flight["origin_code"], "CGK")
        self.assertEqual(bali_flight["destination_code"], "DPS")
        self.assertTrue(bali_flight["number"].startswith("JT"))
        self.assertIn("departure", bali_flight)
        self.assertIn("arrival", bali_flight)
        self.assertIn("duration", bali_flight)

    def test_transport_tickets_can_be_sorted_by_duration_and_departure(self):
        for mode in ("flight", "train", "ship"):
            with self.subTest(mode=mode):
                duration_response = self.client.get(
                    "/api/tickets/",
                    {"mode": mode, "action": "sort", "sort_by": "duration"},
                )
                departure_response = self.client.get(
                    "/api/tickets/",
                    {"mode": mode, "action": "sort", "sort_by": "departure"},
                )

                self.assertEqual(duration_response.status_code, 200)
                self.assertEqual(departure_response.status_code, 200)
                duration_tickets = duration_response.json()["tickets"]
                departure_tickets = departure_response.json()["tickets"]
                duration_minutes = [
                    sum(
                        int(value) * {"d": 1440, "h": 60, "m": 1}[unit]
                        for value, unit in re.findall(
                            r"(\d+)(d|h|m)", ticket["duration"]
                        )
                    )
                    for ticket in duration_tickets
                ]
                departures = [
                    ticket["departure"] for ticket in departure_tickets
                ]
                self.assertEqual(duration_minutes, sorted(duration_minutes))
                self.assertEqual(departures, sorted(departures))
                self.assertIn("duration", duration_response.json()["log"])
                self.assertIn("departure time", departure_response.json()["log"])

    def test_non_transport_categories_reject_duration_sorting(self):
        invalid_order = self.client.get(
            "/api/tickets/",
            {"action": "sort", "sort_by": "arrival"},
        )
        unsupported_category = self.client.get(
            "/api/tickets/",
            {"mode": "hotel", "action": "sort", "sort_by": "duration"},
        )

        self.assertEqual(invalid_order.status_code, 400)
        self.assertEqual(unsupported_category.status_code, 400)

    def test_search_supports_iata_origin_and_destination(self):
        response = self.client.get(
            "/api/tickets/",
            {
                "mode": "flight",
                "action": "search",
                "origin": "CGK",
                "destination": "DPS",
            },
        )

        data = response.json()
        self.assertEqual(response.status_code, 200)
        matches = [data["tickets"][index] for index in data["matching_indices"]]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["destination"], "Bali")

    def test_added_flight_routes_have_route_specific_durations_and_numbers(self):
        response = self.client.get("/api/tickets/", {"action": "sort"})
        self.assertEqual(response.status_code, 200)
        tickets = response.json()["tickets"]

        new_york_to_san_francisco = next(
            ticket for ticket in tickets
            if ticket["origin_code"] == "JFK"
            and ticket["destination_code"] == "SFO"
        )
        singapore_to_new_york = next(
            ticket for ticket in tickets
            if ticket["origin_code"] == "SIN"
            and ticket["destination_code"] == "JFK"
        )
        self.assertEqual(new_york_to_san_francisco["duration"], "6h 00m")
        self.assertEqual(singapore_to_new_york["duration"], "18h 25m")
        self.assertTrue(
            all(
                int(ticket["duration"].split("h")[0]) * 60
                + int(ticket["duration"].split("h")[1].split("m")[0].strip())
                <= 20 * 60
                for ticket in tickets
            )
        )
        self.assertTrue(any(ticket["origin"] != "Jakarta" for ticket in tickets))
        self.assertTrue(all(ticket["number"] for ticket in tickets))
        self.assertEqual(
            len({ticket["number"] for ticket in tickets}),
            len(tickets),
        )

    def test_train_search_returns_route_number_and_schedule(self):
        response = self.client.get(
            "/api/tickets/",
            {"mode": "train", "action": "search", "origin": "Jakarta"},
        )

        data = response.json()
        self.assertEqual(response.status_code, 200)
        tickets = [data["tickets"][index] for index in data["matching_indices"]]
        ticket = next(
            item for item in tickets if item["provider"] == "Argo Bromo Anggrek"
        )
        self.assertEqual(ticket["provider"], "Argo Bromo Anggrek")
        self.assertEqual(ticket["number"], "1")
        self.assertEqual(ticket["departure"], "08:20")
        self.assertEqual(ticket["arrival"], "19:35")

    def test_ship_and_hotel_catalogs_are_available(self):
        ship_data = self.client.get(
            "/api/tickets/", {"mode": "ship", "action": "sort"}
        ).json()
        hotel_data = self.client.get(
            "/api/tickets/", {"mode": "hotel", "action": "sort"}
        ).json()

        self.assertTrue(any(ticket["number"].startswith("KM") for ticket in ship_data["tickets"]))
        self.assertTrue(all("duration" in ticket for ticket in ship_data["tickets"]))
        self.assertTrue(all("rating" in ticket for ticket in hotel_data["tickets"]))
        self.assertTrue(all("check_in" in ticket for ticket in hotel_data["tickets"]))

    def test_search_requires_a_filter_and_rejects_unknown_mode(self):
        missing_filter = self.client.get(
            "/api/tickets/", {"action": "search"}
        )
        unknown_mode = self.client.get(
            "/api/tickets/", {"mode": "bus", "action": "sort"}
        )

        self.assertEqual(missing_filter.status_code, 400)
        self.assertEqual(unknown_mode.status_code, 400)

    def test_search_matches_provider_and_destination_together(self):
        response = self.client.get(
            "/api/tickets/",
            {
                "action": "search",
                "destination": "Singapore",
                "provider": "Garuda",
            },
        )

        data = response.json()
        matches = [data["tickets"][index] for index in data["matching_indices"]]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["provider"], "Garuda Indonesia")
