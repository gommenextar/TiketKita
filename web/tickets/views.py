import json
import subprocess
from pathlib import Path

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


PROJECT_ROOT = Path(settings.BASE_DIR).parent
CPP_PROGRAM = PROJECT_ROOT / "cpp" / "algorithms.exe"


def home(request):
    return render(request, "tickets/home.html")


def ticket_api(request):
    action = request.GET.get("action", "sort")
    destination = request.GET.get("destination", "")
    airline = request.GET.get("airline", "")

    if action not in ("sort", "search"):
        return JsonResponse({"error": "Invalid action"}, status=400)

    command = [str(CPP_PROGRAM), action]

    destination = destination.strip()
    airline = airline.strip()

    if action == "search" and not destination and not airline:
        return JsonResponse(
            {"error": "Enter a destination or airline to search."},
            status=400,
        )

    if destination:
        command.extend(["--destination", destination])
    if airline:
        command.extend(["--airline", airline])

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=5,
            check=True,
        )
        data = json.loads(result.stdout)

        # Convert escaped newline characters in the log into real line breaks.
        data["log"] = data["log"].replace("\\n", "\n")

        return JsonResponse(data)

    except subprocess.CalledProcessError:
        return JsonResponse(
            {"error": "The C++ program failed to run"}, status=500
        )
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return JsonResponse(
            {"error": "Could not process the C++ result"}, status=500
        )
