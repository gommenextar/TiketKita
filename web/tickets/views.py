from django.http import Http404, JsonResponse
from django.shortcuts import render

from .catalog import CATALOGS, PAGE_INFO


def home(request):
    return render(request, "tickets/landing.html")


def category_page(request, mode):
    page = PAGE_INFO[mode]
    return render(request, "tickets/home.html", {
        "mode": mode,
        "page": page,
    })


def trip_detail(request, mode, ticket_id):
    if mode not in ("flight", "train", "ship"):
        raise Http404("Trip not found.")
    ticket = next(
        (item for item in CATALOGS[mode] if item["id"] == ticket_id),
        None,
    )
    if ticket is None:
        raise Http404("Trip not found.")
    return render(request, "tickets/trip_detail.html", {
        "mode": mode,
        "page": PAGE_INFO[mode],
        "ticket": ticket,
        "formatted_price": f"Rp{ticket['price']:,}".replace(",", "."),
    })


def _matches(ticket, query, fields):
    query = query.casefold()
    return any(query in str(ticket.get(field, "")).casefold() for field in fields)


def _duration_minutes(duration):
    units = {"d": 1440, "h": 60, "m": 1}
    total_minutes = 0
    number = ""
    for character in duration:
        if character.isdigit():
            number += character
        elif character in units and number:
            total_minutes += int(number) * units[character]
            number = ""
    return total_minutes


def _bubble_sort(tickets, sort_by):
    tickets = [ticket.copy() for ticket in tickets]
    sort_values = {
        "price": lambda ticket: ticket["price"],
        "duration": lambda ticket: _duration_minutes(ticket["duration"]),
        "departure": lambda ticket: (
            int(ticket["departure"][:2]) * 60 + int(ticket["departure"][3:])
        ),
    }
    sort_labels = {
        "price": "price (ascending)",
        "duration": "duration (shortest first)",
        "departure": "departure time (earliest first)",
    }
    get_sort_value = sort_values[sort_by]
    log = [f"Django Bubble Sort: sorting by {sort_labels[sort_by]}"]
    for pass_number in range(len(tickets) - 1):
        swapped = False
        for index in range(len(tickets) - pass_number - 1):
            left = tickets[index]
            right = tickets[index + 1]
            log.append(
                f"Compare {left['provider']} to {left['destination']} "
                f"({get_sort_value(left)}) with {right['provider']} to "
                f"{right['destination']} ({get_sort_value(right)})"
            )
            if get_sort_value(left) > get_sort_value(right):
                tickets[index], tickets[index + 1] = right, left
                swapped = True
                log.append(" -> SWAP")
            else:
                log.append(" -> No swap")
        if not swapped:
            break
    log.append("Sorting complete.")
    return tickets, log


def _linear_search(tickets, origin, destination, provider, mode):
    log = ["Django Linear Search:"]
    filters = []
    if origin:
        filters.append(("origin", origin, ("origin", "origin_code")))
    if destination:
        destination_fields = ("destination", "destination_code")
        filters.append(("destination", destination, destination_fields))
    if provider:
        provider_field = "provider"
        filters.append((provider_field, provider, (provider_field, "airline")))

    log.append(", ".join(f'{name} "{query}"' for name, query, _ in filters))
    matching_indices = []
    for index, ticket in enumerate(tickets):
        matches = all(
            _matches(ticket, query, fields)
            for _, query, fields in filters
        )
        log.append(
            f"Step {index + 1}: Check {ticket['provider']} "
            f"{ticket.get('origin', '')} to {ticket['destination']}"
            f"{' -> MATCH FOUND' if matches else ' -> No match'}"
        )
        if matches:
            matching_indices.append(index)
    if matching_indices:
        log.append(
            f"Search complete: {len(matching_indices)} matching "
            f"ticket(s) in {mode}."
        )
    else:
        log.append("No matching tickets found.")
    return matching_indices, log


def ticket_api(request):
    mode = request.GET.get("mode", "flight").strip().lower()
    action = request.GET.get("action", "sort").strip().lower()
    sort_by = request.GET.get("sort_by", "price").strip().lower()
    origin = request.GET.get("origin", "").strip()
    destination = request.GET.get("destination", "").strip()
    provider = request.GET.get("provider", "").strip()

    if mode not in CATALOGS:
        return JsonResponse({"error": "Invalid ticket category."}, status=400)
    if action not in ("sort", "search"):
        return JsonResponse({"error": "Invalid action."}, status=400)
    if sort_by not in ("price", "duration", "departure"):
        return JsonResponse({"error": "Invalid sort order."}, status=400)
    if mode == "hotel" and sort_by != "price":
        return JsonResponse(
            {"error": "Duration and departure sorting are only available for transport."},
            status=400,
        )
    if action == "search" and not any((origin, destination, provider)):
        return JsonResponse(
            {"error": "Enter an origin, destination, or provider to search."},
            status=400,
        )
    if mode == "hotel" and origin:
        return JsonResponse(
            {"error": "Origin search is not available for hotels."},
            status=400,
        )

    tickets, log = _bubble_sort(CATALOGS[mode], sort_by)
    matching_indices = []
    if any((origin, destination, provider)):
        matching_indices, search_log = _linear_search(
            tickets, origin, destination, provider, mode
        )
        log.extend(search_log)
    return JsonResponse({
        "tickets": tickets,
        "matching_indices": matching_indices,
        "log": "\n".join(log),
        "found_index": matching_indices[0] if matching_indices else -1,
    })
