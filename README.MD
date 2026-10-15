# TiketKita

A simple ticket-booking website inspired by online travel platforms, developed as a Data Structures and Algorithms project.

TiketKita combines a Django web application with C++ sorting and searching algorithms to demonstrate how algorithms can be integrated into a web-based interface.

## Features

- **Ticket Listing:** Displays sample airline tickets and their prices.
- **Ticket Sorting:** Uses Bubble Sort to arrange tickets from cheapest to most expensive.
- **Destination Search:** Uses Linear Search to find tickets by destination.
- **Algorithm Logs:** Displays the steps performed by the sorting and searching algorithms.
- **Interactive Web Interface:** Built with Django, HTML, CSS, and JavaScript.
- **C++ Integration:** Executes the sorting and searching algorithms through the Django backend.

## Technologies Used

- Python 3.12
- Django
- C++
- GCC / G++ compiler
- HTML, CSS, and JavaScript
- Git and GitHub

## Project Structure

```text
TiketKita/
├── cpp/
│   ├── algorithms.cpp
│   └── algorithms.exe       # Compiled locally if needed
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
├── requirements.txt         # If included in the repository
└── README.md
```

## How to Run from Scratch

Follow the instructions for your operating system.

### 1. Install the Prerequisites

Install the following software:

- **Python:** [Download Python](https://www.python.org/downloads/)
- **Git:** [Download Git](https://git-scm.com/downloads)
- **C++ compiler:** Install GCC/G++ using the instructions for your operating system below.
- **Visual Studio Code (optional):** [Download VS Code](https://code.visualstudio.com/)

Verify your installations in a terminal:

```bash
python --version
git --version
g++ --version
```

On Linux and macOS, you may need to use `python3 --version` instead of `python --version`.

### 2. Install G++ on Windows

The following instructions use MSYS2 and its UCRT64 environment.

1. Download and install [MSYS2](https://www.msys2.org/).
2. Open the **MSYS2 UCRT64** terminal.
3. Install GCC by running:

   ```bash
   pacman -S --needed mingw-w64-ucrt-x86_64-gcc
   ```

4. Add the following directory to your Windows `PATH` environment variable:

   ```text
   C:\msys64\ucrt64\bin
   ```

5. Restart your terminal and verify the installation:

   ```powershell
   g++ --version
   ```

### 3. Install G++ on Linux

For Ubuntu or Debian-based distributions, open a terminal and run:

```bash
sudo apt update
sudo apt install build-essential
```

For Fedora, run:

```bash
sudo dnf install gcc-c++
```

For other distributions, install the GCC C++ compiler using your distribution's package manager.

Verify the installation:

```bash
g++ --version
```

### 4. Install a C++ Compiler on macOS

On macOS, install Apple's Command Line Tools by running:

```bash
xcode-select --install
```

Follow the installation prompts. This provides the C++ compiler toolchain needed to compile the project.

Verify that a compatible compiler is available:

```bash
g++ --version
```

macOS may report Apple Clang rather than GNU GCC. That is normal; the compiler supports the command used in this project.

### 5. Download the Project

Open a terminal and run:

```bash
git clone https://github.com/gommenextar/TiketKita.git
cd TiketKita
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

All remaining commands should be run from the **TiketKita project root**, unless stated otherwise.

### 6. Create a Python Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python installations.

**Windows — PowerShell:**

```powershell
py -3.12 -m venv .venv
```

**Linux and macOS:**

```bash
python3 -m venv .venv
```

If the virtual environment creation fails on Linux, install the Python virtual environment package through your distribution's package manager.

### 7. Install the Python Dependencies

If the repository contains `requirements.txt`, install its dependencies.

**Windows — PowerShell:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux and macOS:**

```bash
./.venv/bin/python -m pip install -r requirements.txt
```

If `requirements.txt` is not included, install Django directly instead.

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m pip install django
```

**Linux and macOS:**

```bash
./.venv/bin/python -m pip install django
```

Verify the Django installation:

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m django --version
```

**Linux and macOS:**

```bash
./.venv/bin/python -m django --version
```

### 8. Compile the C++ Program

The Django backend executes the compiled C++ program. Compile it from the project root:

```bash
g++ cpp/algorithms.cpp -o cpp/algorithms.exe
```

This command deliberately uses the filename `algorithms.exe` on every platform because the Django backend expects that exact path. On Linux and macOS, the `.exe` extension is simply part of the filename.

If compilation succeeds, the executable will be created inside the `cpp/` directory.

**Important:** Recompile the C++ program whenever you modify `algorithms.cpp`.

### 9. Check the Django Application

Run Django's configuration check.

**Windows:**

```powershell
.\.venv\Scripts\python.exe web\manage.py check
```

**Linux and macOS:**

```bash
./.venv/bin/python web/manage.py check
```

If the check reports errors, resolve them before starting the server.

### 10. Start the Development Server

Run the Django development server from the project root.

**Windows — PowerShell:**

```powershell
.\.venv\Scripts\python.exe web\manage.py runserver
```

**Linux and macOS:**

```bash
./.venv/bin/python web/manage.py runserver
```

When the server starts successfully, open the following address in your browser:

http://127.0.0.1:8000/

Keep the terminal running while using the website. Press `Ctrl + C` to stop the server.

## How to Use TiketKita

1. **View Tickets:** Open the homepage to see the available sample tickets.
2. **Search for a Destination:** Enter a destination, such as `Surabaya` or `Bali`, and click the search button to find a matching ticket.
3. **Sort Tickets:** Click the sorting button to arrange tickets from the lowest price to the highest price.
4. **View Algorithm Logs:** Open the algorithm log panel to inspect the steps performed by the C++ sorting or searching algorithm.
5. **Select a Ticket:** Click the ticket selection button to see the demonstration message.

The ticket selection feature is for demonstration only. The application does not make real bookings.

## Algorithms Demonstrated

### Bubble Sort

Bubble Sort sorts tickets by price in ascending order by repeatedly comparing adjacent elements and swapping them when they are in the wrong order.

- Average time complexity: O(n²)
- Worst-case time complexity: O(n²)
- Best-case time complexity: O(n) when implemented with an early-exit optimization

The application displays the sorting process through an algorithm log.

### Linear Search

Linear Search checks tickets one by one until it finds a matching destination or reaches the end of the list.

- Average time complexity: O(n)
- Worst-case time complexity: O(n)
- Best-case time complexity: O(1)

The application displays the search process through an algorithm log.

### Data Structures

The C++ implementation demonstrates the use of arrays, pointers, and structs to represent and process ticket information.

## Troubleshooting

### `g++` Is Not Recognized

Make sure a compatible C++ compiler is installed and its executable directory is included in your system's `PATH`. Restart your terminal after changing the environment variables.

### The C++ Executable Cannot Be Found

Compile `cpp/algorithms.cpp` from the project root and confirm that the resulting file is located at `cpp/algorithms.exe`.

### Django Cannot Be Imported

Make sure the virtual environment was created successfully and the project's Python dependencies were installed. Use the virtual environment's Python executable when running Django commands.

### The Website Does Not Load

Check that the development server is running and that the terminal does not display configuration or runtime errors.

## Limitations

- Ticket data is sample data and does not represent live airline availability.
- No real payment, booking, or airline inventory service is connected.
- The website runs locally and requires separate deployment to become publicly accessible as a web application.
- The C++ program must be compiled on the target operating system.
- Python dependencies and a compatible C++ compiler must be installed before running the application.

## Author

Developed as a student project demonstrating data structures, algorithms, C++ integration, and web development with Django.