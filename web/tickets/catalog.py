from datetime import datetime, timedelta


AIRPORTS = {
    "Jakarta": "CGK",
    "Bali": "DPS",
    "Surabaya": "SUB",
    "Yogyakarta": "YIA",
    "Medan": "KNO",
    "Makassar": "UPG",
    "Balikpapan": "BPN",
    "Lombok": "LOP",
    "Pontianak": "PNK",
    "Banjarmasin": "BDJ",
    "Manado": "MDC",
    "Labuan Bajo": "LBJ",
    "Kupang": "KOE",
    "Palembang": "PLM",
    "Banda Aceh": "BTJ",
    "Jayapura": "DJJ",
    "Ternate": "TTE",
    "Singapore": "SIN",
    "Kuala Lumpur": "KUL",
    "Bangkok": "BKK",
    "Tokyo": "HND",
    "Hong Kong": "HKG",
    "Dubai": "DXB",
    "Doha": "DOH",
    "Istanbul": "IST",
    "Amsterdam": "AMS",
    "Frankfurt": "FRA",
    "London": "LHR",
    "Paris": "CDG",
    "Sydney": "SYD",
    "New York": "JFK",
    "Los Angeles": "LAX",
    "Toronto": "YYZ",
    "San Francisco": "SFO",
    "Seoul": "ICN",
}

AIRLINES = {
    "Garuda Indonesia": "GA",
    "Lion Air": "JT",
    "Citilink": "QG",
    "Batik Air": "ID",
    "AirAsia": "QZ",
    "Sriwijaya Air": "SJ",
    "Wings Air": "IW",
    "Xpress Air": "XN",
    "Super Air Jet": "IU",
    "Pelita Air": "IP",
    "Singapore Airlines": "SQ",
    "Malaysia Airlines": "MH",
    "Cathay Pacific": "CX",
    "Scoot": "TR",
    "Emirates": "EK",
    "Qatar Airways": "QR",
    "Turkish Airlines": "TK",
    "KLM Royal Dutch Airlines": "KL",
    "Lufthansa": "LH",
    "British Airways": "BA",
    "Air France": "AF",
    "United Airlines": "UA",
}

FLIGHT_ROWS = [
    ("Garuda Indonesia", "Surabaya", 1200000),
    ("Lion Air", "Bali", 650000),
    ("Citilink", "Surabaya", 800000),
    ("Batik Air", "Yogyakarta", 950000),
    ("AirAsia", "Medan", 700000),
    ("Sriwijaya Air", "Makassar", 850000),
    ("Wings Air", "Balikpapan", 600000),
    ("Garuda Indonesia", "Lombok", 1100000),
    ("Lion Air", "Pontianak", 720000),
    ("Citilink", "Banjarmasin", 680000),
    ("Batik Air", "Manado", 1050000),
    ("AirAsia", "Labuan Bajo", 980000),
    ("Wings Air", "Kupang", 870000),
    ("Super Air Jet", "Palembang", 640000),
    ("Pelita Air", "Banda Aceh", 920000),
    ("Garuda Indonesia", "Jayapura", 1850000),
    ("Lion Air", "Ternate", 1150000),
    ("Garuda Indonesia", "Singapore", 2100000),
]

REGIONAL_FLIGHT_ROWS = [
    ("AirAsia", "Singapore", "Kuala Lumpur", 950000),
    ("Malaysia Airlines", "Kuala Lumpur", "Singapore", 1000000),
    ("Singapore Airlines", "Bali", "Singapore", 2300000),
    ("Batik Air", "Surabaya", "Bali", 850000),
    ("AirAsia", "Medan", "Kuala Lumpur", 1200000),
    ("Garuda Indonesia", "Makassar", "Bali", 1750000),
    ("Lion Air", "Balikpapan", "Surabaya", 1050000),
    ("Super Air Jet", "Lombok", "Bali", 700000),
    ("Malaysia Airlines", "Pontianak", "Kuala Lumpur", 1550000),
    ("Citilink", "Banjarmasin", "Surabaya", 850000),
    ("Batik Air", "Manado", "Makassar", 1150000),
    ("Wings Air", "Labuan Bajo", "Bali", 750000),
    ("Garuda Indonesia", "Kupang", "Bali", 1800000),
    ("AirAsia", "Palembang", "Singapore", 1250000),
    ("Malaysia Airlines", "Banda Aceh", "Kuala Lumpur", 1400000),
    ("Garuda Indonesia", "Jayapura", "Makassar", 2900000),
    ("Lion Air", "Ternate", "Manado", 900000),
    ("Qatar Airways", "Doha", "Dubai", 1850000),
]

ADDITIONAL_FLIGHT_ROWS = [
    ("Singapore Airlines", "Singapore", "New York", 14500000),
    ("United Airlines", "New York", "San Francisco", 4200000),
    ("United Airlines", "San Francisco", "New York", 4200000),
    ("United Airlines", "New York", "Los Angeles", 3900000),
    ("Qatar Airways", "Doha", "San Francisco", 13800000),
    ("Cathay Pacific", "Hong Kong", "Toronto", 9700000),
    ("Qatar Airways", "Doha", "Toronto", 8200000),
    ("Cathay Pacific", "Hong Kong", "New York", 11200000),
    ("Emirates", "Dubai", "New York", 9000000),
    ("Singapore Airlines", "Singapore", "Tokyo", 4200000),
    ("Cathay Pacific", "Tokyo", "Seoul", 1800000),
    ("British Airways", "London", "Paris", 1600000),
    ("Emirates", "Dubai", "London", 3800000),
    ("Singapore Airlines", "Sydney", "Singapore", 5100000),
    ("Singapore Airlines", "Bali", "Singapore", 2300000),
    ("Malaysia Airlines", "Kuala Lumpur", "Bangkok", 1500000),
]

# Approximate flight durations in minutes.
# Values are estimates and may vary by airline, route, and season.
# For routes without nonstop service, these are rough estimates,
# not guaranteed total itinerary times including connections.

FLIGHT_DURATIONS = {
    # Domestic Indonesia
    ("Jakarta", "Surabaya"): 90,
    ("Jakarta", "Bali"): 115,
    ("Jakarta", "Yogyakarta"): 75,
    ("Jakarta", "Medan"): 145,
    ("Jakarta", "Makassar"): 150,
    ("Jakarta", "Balikpapan"): 130,
    ("Jakarta", "Lombok"): 115,
    ("Jakarta", "Pontianak"): 90,
    ("Jakarta", "Banjarmasin"): 105,
    ("Jakarta", "Manado"): 190,
    ("Jakarta", "Labuan Bajo"): 150,
    ("Jakarta", "Kupang"): 180,
    ("Jakarta", "Palembang"): 75,
    ("Jakarta", "Banda Aceh"): 165,
    ("Jakarta", "Jayapura"): 320,
    ("Jakarta", "Ternate"): 210,

    # Southeast Asia
    ("Jakarta", "Singapore"): 105,
    ("Jakarta", "Kuala Lumpur"): 125,
    ("Jakarta", "Bangkok"): 210,
    ("Singapore", "Kuala Lumpur"): 80,
    ("Kuala Lumpur", "Singapore"): 80,
    ("Surabaya", "Bali"): 60,
    ("Medan", "Kuala Lumpur"): 75,
    ("Makassar", "Bali"): 90,
    ("Balikpapan", "Surabaya"): 105,
    ("Lombok", "Bali"): 40,
    ("Pontianak", "Kuala Lumpur"): 120,
    ("Banjarmasin", "Surabaya"): 75,
    ("Manado", "Makassar"): 105,
    ("Labuan Bajo", "Bali"): 80,
    ("Kupang", "Bali"): 135,
    ("Palembang", "Singapore"): 75,
    ("Banda Aceh", "Kuala Lumpur"): 90,
    ("Jayapura", "Makassar"): 180,
    ("Ternate", "Manado"): 70,
    ("Doha", "Dubai"): 80,
    ("Kuala Lumpur", "Bangkok"): 120,

    # East Asia
    ("Jakarta", "Tokyo"): 450,
    ("Jakarta", "Hong Kong"): 310,
    ("Singapore", "Tokyo"): 430,
    ("Tokyo", "Seoul"): 150,

    # Middle East
    ("Jakarta", "Dubai"): 490,
    ("Jakarta", "Doha"): 510,
    ("Jakarta", "Istanbul"): 710,

    # Europe
    ("Jakarta", "Amsterdam"): 890,
    ("Jakarta", "Frankfurt"): 850,
    ("Jakarta", "London"): 900,
    ("Jakarta", "Paris"): 850,
    ("London", "Paris"): 75,
    ("Dubai", "London"): 450,

    # Australia and Oceania
    ("Jakarta", "Sydney"): 405,
    ("Sydney", "Singapore"): 465,
    ("Bali", "Singapore"): 165,

    # North America
    ("Jakarta", "Los Angeles"): 1080,
    ("Singapore", "New York"): 1105,
    ("New York", "San Francisco"): 360,
    ("San Francisco", "New York"): 330,
    ("New York", "Los Angeles"): 375,
    ("Doha", "San Francisco"): 945,
    ("Hong Kong", "Toronto"): 900,
    ("Doha", "Toronto"): 845,
    ("Hong Kong", "New York"): 960,
    ("Dubai", "New York"): 840,
}


def build_flights():
    flights = []
    flight_rows = [
        (airline, "Jakarta", destination, price)
        for airline, destination, price in FLIGHT_ROWS
    ] + REGIONAL_FLIGHT_ROWS + ADDITIONAL_FLIGHT_ROWS
    for ticket_id, (airline, origin, destination, price) in enumerate(
        flight_rows, start=1
    ):
        duration_minutes = FLIGHT_DURATIONS[(origin, destination)]
        departure = datetime.strptime(
            f"{5 + ticket_id % 17:02}:00", "%H:%M"
        )
        arrival = (departure + timedelta(minutes=duration_minutes)).strftime("%H:%M")
        flights.append({
            "id": ticket_id,
            "provider": airline,
            "airline": airline,
            "number": f"{AIRLINES[airline]}{100 + ticket_id}",
            "origin": origin,
            "origin_code": AIRPORTS[origin],
            "destination": destination,
            "destination_code": AIRPORTS.get(destination, ""),
            "departure": departure.strftime("%H:%M"),
            "arrival": arrival,
            "duration": f"{duration_minutes // 60}h {duration_minutes % 60:02}m",
            "price": price,
        })
    return flights


FLIGHTS = build_flights()

TRAINS = [
    {"id": 1, "provider": "Argo Bromo Anggrek", "number": "1",
     "origin": "Jakarta", "destination": "Surabaya", "departure": "08:20",
     "arrival": "19:35", "duration": "11h 15m", "price": 750000},
    {"id": 2, "provider": "Argo Parahyangan", "number": "44",
     "origin": "Jakarta", "destination": "Bandung", "departure": "07:30",
     "arrival": "10:20", "duration": "2h 50m", "price": 150000},
    {"id": 3, "provider": "Taksaka", "number": "46",
     "origin": "Yogyakarta", "destination": "Jakarta", "departure": "09:00",
     "arrival": "16:10", "duration": "7h 10m", "price": 390000},
    {"id": 4, "provider": "Gajayana", "number": "35",
     "origin": "Jakarta", "destination": "Malang", "departure": "18:50",
     "arrival": "09:15", "duration": "14h 25m", "price": 650000},
    {"id": 5, "provider": "Lodaya", "number": "92",
     "origin": "Bandung", "destination": "Yogyakarta", "departure": "06:30",
     "arrival": "14:00", "duration": "7h 30m", "price": 290000},
    {"id": 6, "provider": "Matarmaja", "number": "281",
     "origin": "Malang", "destination": "Jakarta", "departure": "17:30",
     "arrival": "10:40", "duration": "17h 10m", "price": 250000},
]

SHIPS = [
    {"id": 1, "provider": "PELNI", "number": "KM Gunung Dempo",
     "origin": "Jakarta", "destination": "Makassar", "departure": "15:00",
     "arrival": "06:00", "duration": "3d 15h", "price": 560000},
    {"id": 2, "provider": "PELNI", "number": "KM Kelud",
     "origin": "Jakarta", "destination": "Medan", "departure": "08:00",
     "arrival": "12:00", "duration": "2d 4h", "price": 450000},
    {"id": 3, "provider": "PELNI", "number": "KM Sinabung",
     "origin": "Makassar", "destination": "Surabaya", "departure": "20:00",
     "arrival": "08:00", "duration": "1d 12h", "price": 380000},
    {"id": 4, "provider": "PELNI", "number": "KM Awu",
     "origin": "Surabaya", "destination": "Bali", "departure": "16:00",
     "arrival": "04:00", "duration": "12h", "price": 180000},
    {"id": 5, "provider": "ASDP Ferry", "number": "KMP Nusa Jaya",
     "origin": "Bali", "destination": "Lombok", "departure": "09:00",
     "arrival": "13:30", "duration": "4h 30m", "price": 125000},
    {"id": 6, "provider": "ASDP Ferry", "number": "KMP Prima Nusantara",
     "origin": "Merak", "destination": "Bakauheni", "departure": "10:00",
     "arrival": "12:00", "duration": "2h", "price": 65000},
]

HOTELS = [
    {"id": 1, "provider": "The Jakarta Hotel", "destination": "Jakarta",
     "rating": 5, "check_in": "14:00", "check_out": "12:00",
     "duration": "1 night", "price": 1250000},
    {"id": 2, "provider": "Bali Beach Resort", "destination": "Bali",
     "rating": 5, "check_in": "15:00", "check_out": "11:00",
     "duration": "1 night", "price": 1850000},
    {"id": 3, "provider": "Surabaya City Stay", "destination": "Surabaya",
     "rating": 4, "check_in": "14:00", "check_out": "12:00",
     "duration": "1 night", "price": 680000},
    {"id": 4, "provider": "Yogyakarta Heritage Inn", "destination": "Yogyakarta",
     "rating": 4, "check_in": "14:00", "check_out": "12:00",
     "duration": "1 night", "price": 540000},
    {"id": 5, "provider": "Singapore Garden Hotel", "destination": "Singapore",
     "rating": 4, "check_in": "15:00", "check_out": "11:00",
     "duration": "1 night", "price": 2200000},
    {"id": 6, "provider": "Kuala Lumpur Central Suites", "destination": "Kuala Lumpur",
     "rating": 4, "check_in": "15:00", "check_out": "12:00",
     "duration": "1 night", "price": 950000},
]

CATALOGS = {
    "flight": FLIGHTS,
    "train": TRAINS,
    "ship": SHIPS,
    "hotel": HOTELS,
}

PAGE_INFO = {
    "flight": {
        "title": "Flight tickets",
        "label": "✈ Flight Tickets",
        "headline": "Fly somewhere new.",
        "description": "Compare flight routes, airport codes, departure times, and fares.",
        "provider_label": "AIRLINE",
    },
    "train": {
        "title": "Train tickets",
        "label": "🚆 Train Tickets",
        "headline": "Take the scenic route.",
        "description": "Explore train services, station-to-station routes, schedules, and fares.",
        "provider_label": "TRAIN OPERATOR",
    },
    "ship": {
        "title": "Ship tickets",
        "label": "⛴ Ship Tickets",
        "headline": "Make your next trip a voyage.",
        "description": "Compare ferry and ship routes, departure times, journey durations, and fares.",
        "provider_label": "SHIP OPERATOR",
    },
    "hotel": {
        "title": "Hotels",
        "label": "⌂ Hotels",
        "headline": "Find a place to stay.",
        "description": "Browse sample stays by destination and compare nightly rates.",
        "provider_label": "HOTEL",
    },
}
