# TiketKita

A simple ticket-booking website inspired by online travel platforms, built as a data structures and algorithms project.

## Features

- **Ticket listing:** Display sample airline tickets and prices.
- **Sorting:** Bubble Sort orders tickets from cheapest to most expensive.
- **Searching:** Linear Search finds tickets by destination.
- **Algorithm logs:** View sorting and searching steps through an expandable log panel.
- **Web interface:** Django backend with HTML, CSS, and JavaScript.
- **C++ integration:** Sorting and searching algorithms are implemented in C++.

## Technologies

- Python 3.12
- Django
- C++
- HTML, CSS, and JavaScript
- Visual Studio Code

## Project Structure

```text
TiketKita/
├── cpp/
│   ├── algorithms.cpp
│   └── algorithms.exe
├── web/
│   ├── manage.py
│   ├── config/
│   └── tickets/
│       ├── views.py
│       ├── urls.py
│       ├── templates/
│       │   └── tickets/
│       │       └── home.html
│       └── static/
│           └── tickets/
│               ├── style.css
│               └── script.js
├── .gitignore
└── README.md
```

*The compiled executable may not be included in the repository. Compile it locally if necessary.*

## How to Run from Scratch

Follow these instructions to set up and run TiketKita on a new Windows computer.

### 1. Install the prerequisites

Install the following software:

- **Python 3.12:** https://www.python.org/downloads/
- **Visual Studio Code:** https://code.visualstudio.com/
- **Git:** https://git-scm.com/downloads
- **MinGW-w64 / g++:** A C++ compiler compatible with your Windows environment.

Verify your installations in the VS Code terminal:

```powershell
python --version
git --version
g++ --version
```

### 2. Download the project

Open PowerShell or the VS Code terminal and run:

```powershell
git clone https://github.com/gommenextar/TiketKita.git
cd TiketKita
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

Open the extracted `TiketKita` folder in VS Code.

### 3. Create a Python virtual environment

From the project root, run:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can avoid changing the execution policy and invoke the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install django
```

Use the virtual environment's Python for the remaining commands if activation fails.

### 4. Install Django

With the virtual environment activated, run:

```powershell
python -m pip install django
```

Verify the installation:

```powershell
python -m django --version
```

### 5. Compile the C++ program

Make sure the C++ source file is available in `cpp/`. From the project root, run:

```powershell
g++ .\cpp\algorithms.cpp -o .\cpp\algorithms.exe
```

This creates the executable used by the Django application.

**Important:** The C++ program must accept the commands and arguments expected by `views.py`, such as `sort` and `search` followed by a destination. Its output must also match the JSON format expected by Django.

### 6. Check the Django configuration

Navigate to the Django application directory:

```powershell
cd web
```

Confirm that the project contains `manage.py`, the `config` package, and the `tickets` application.

If dependencies are missing, install them using the virtual environment's Python. The commands below assume the environment is located in the project root.

From the project root, you can use:

```powershell
.\.venv\Scripts\python.exe -m django check
```

If you have a Django `requirements.txt` file, install its dependencies with:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 7. Run database migrations if needed

If the project uses Django models or requires a local database, run this from the `web` directory:

```powershell
..\ .venv\Scripts\python.exe manage.py migrate
```

If the command above is copied into PowerShell, remove the space after `..\` so the executable path is correct. The correct command is:

```powershell
..\.venv\Scripts\python.exe manage.py migrate
```

If the application does not use database-backed features, migrations may not be necessary for its ticket demonstration.

### 8. Start the Django development server

From the `web` directory, run:

```powershell
..\ .venv\Scripts\python.exe manage.py runserver
```

The correct executable path, without the extra space, is:

```powershell
..\.venv\Scripts\python.exe manage.py runserver
```

Alternatively, if the virtual environment is activated:

```powershell
python manage.py runserver
```

### 9. Open the website

Visit:

http://127.0.0.1:8000/

The TiketKita homepage should load in your browser.

### 10. Use the website

1. **View tickets:** The homepage initially displays all available sample tickets.
2. **Search:** Enter a destination, such as `Surabaya` or `Bali`, and click **Search Tickets**. Only the matching ticket should be displayed.
3. **Sort:** Click **Sort: Cheapest first** to display all tickets in ascending price order.
4. **View algorithm logs:** Click **Show algorithm log** to inspect the C++ sorting or searching steps. Click again to hide the log.
5. **Select a ticket:** Click **Select ticket** to see the demonstration message. This does not make a real booking.

## Algorithms Demonstrated

### Bubble Sort

Sorts tickets by price in ascending order by repeatedly comparing adjacent tickets and swapping them when they are in the wrong order.

- Average and worst-case time complexity: \(O(n^2)\)

### Linear Search

Checks tickets one by one until a matching destination is found.

- Average and worst-case time complexity: \(O(n)\)

The algorithms demonstrate arrays, pointers, and structs in C++.

## Limitations

- Ticket data is sample data.
- Real airline inventory and booking services are not connected.
- The website runs locally unless deployed to a hosting service.
- The C++ executable must be compiled for the target operating system.
- Python dependencies must be installed before running the application.

## Author

Developed as a student project to demonstrate data structures, algorithms, C++ integration, and web development using Django.
