# TiketKita

A Django travel-listing demo for flights, trains, ships, and hotels. The sample
catalogs and the sorting/search algorithms run in Python on the Django backend;
the browser uses Django's JSON API to display results.

## Features

- Browse flights, trains, ships, and hotels on separate pages.
- Search by origin, destination, and provider. Flight origin and destination
  searches accept city names or airport IATA codes.
- Flight listings show airline flight numbers, route, airport codes, departure,
  arrival, duration, and sample fare.
- Train and ship listings show service/vessel numbers, route, schedule, duration,
  and sample fare. Hotel listings show destination, rating, check-in/out, and
  sample nightly rate.
- Sort by price with Bubble Sort and search with Linear Search; both algorithms
  are implemented in Django and can be inspected in the algorithm log.

## Run locally

Requirements: Python 3.12 or newer and Django (see `requirements.txt`).

From the repository root, create and activate a virtual environment, then
install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the Django development server:

```powershell
.\.venv\Scripts\python.exe web\manage.py runserver
```

Open <http://127.0.0.1:8000/>. Django serves the flight page at the root;
additional pages are `/trains/`, `/ships/`, and `/hotels/`.

## API

`GET /api/tickets/` supports `mode` (`flight`, `train`, `ship`, or `hotel`),
`action` (`sort` or `search`), `origin`, `destination`, and `provider`.

For example:

```text
/api/tickets/?mode=flight&action=search&origin=CGK&destination=DPS
```

## Sample data notice

Listings are hard-coded demonstration data. They are not live schedules,
availability, prices, or a booking service. Flight numbers, timings, and other
service details should be verified with the relevant operator before travel.
