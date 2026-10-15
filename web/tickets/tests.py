import json
from types import SimpleNamespace
from unittest.mock import patch

from django.test import TestCase


class TicketApiTests(TestCase):
    @patch("tickets.views.subprocess.run")
    def test_search_by_airline_passes_airline_filter(self, run):
        run.return_value = SimpleNamespace(
            stdout=json.dumps({
                "tickets": [],
                "matching_indices": [],
                "log": "",
                "found_index": -1,
            })
        )

        response = self.client.get(
            "/api/tickets/", {"action": "search", "airline": "AirAsia"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("--airline", run.call_args.args[0])
        self.assertIn("AirAsia", run.call_args.args[0])

    @patch("tickets.views.subprocess.run")
    def test_search_passes_destination_and_airline_filters(self, run):
        run.return_value = SimpleNamespace(
            stdout=json.dumps({
                "tickets": [],
                "matching_indices": [],
                "log": "",
                "found_index": -1,
            })
        )

        response = self.client.get(
            "/api/tickets/",
            {
                "action": "search",
                "destination": "Singapore",
                "airline": "Garuda",
            },
        )

        self.assertEqual(response.status_code, 200)
        command = run.call_args.args[0]
        self.assertEqual(
            command[1:],
            [
                "search",
                "--destination",
                "Singapore",
                "--airline",
                "Garuda",
            ],
        )

    @patch("tickets.views.subprocess.run")
    def test_search_requires_at_least_one_filter(self, run):
        response = self.client.get("/api/tickets/", {"action": "search"})

        self.assertEqual(response.status_code, 400)
        run.assert_not_called()

    @patch("tickets.views.subprocess.run")
    def test_sort_preserves_destination_and_airline_filters(self, run):
        run.return_value = SimpleNamespace(
            stdout=json.dumps({
                "tickets": [],
                "matching_indices": [],
                "log": "",
                "found_index": -1,
            })
        )

        response = self.client.get(
            "/api/tickets/",
            {
                "action": "sort",
                "destination": "Singapore",
                "airline": "Garuda",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            run.call_args.args[0][1:],
            [
                "sort",
                "--destination",
                "Singapore",
                "--airline",
                "Garuda",
            ],
        )
