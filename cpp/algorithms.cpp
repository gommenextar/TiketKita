
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <limits>
using namespace std;

struct Ticket {
    int id;
    string airline;
    string destination;
    int price;
};

Ticket tickets[] = {
    {1,  "Garuda Indonesia", "Jakarta", 1200000},
    {2,  "Lion Air", "Bali", 650000},
    {3,  "Citilink", "Surabaya", 800000},
    {4,  "Batik Air", "Yogyakarta", 950000},
    {5,  "AirAsia", "Medan", 700000},
    {6,  "Sriwijaya Air", "Makassar", 850000},
    {7,  "Wings Air", "Balikpapan", 600000},
    {8,  "Ngawi JMK Air", "Ngawi", 750000},
    {9,  "Xpress Air", "Ngawi", 900000},

    // Additional domestic flights
    {10, "Garuda Indonesia", "Lombok", 1100000},
    {11, "Lion Air", "Pontianak", 720000},
    {12, "Citilink", "Banjarmasin", 680000},
    {13, "Batik Air", "Manado", 1050000},
    {14, "AirAsia", "Labuan Bajo", 980000},
    {15, "Wings Air", "Kupang", 870000},
    {16, "Super Air Jet", "Palembang", 640000},
    {17, "Pelita Air", "Banda Aceh", 920000},
    {18, "Garuda Indonesia", "Jayapura", 1850000},
    {19, "Lion Air", "Ternate", 1150000},

    // International flights
    {20, "Garuda Indonesia", "Singapore", 2100000},
    {21, "AirAsia", "Kuala Lumpur", 950000},
    {22, "Batik Air", "Bangkok", 1850000},
    {23, "Singapore Airlines", "Singapore", 2800000},
    {24, "Malaysia Airlines", "Kuala Lumpur", 1750000},
    {25, "Garuda Indonesia", "Tokyo", 5800000},
    {26, "AirAsia", "Bangkok", 1450000},
    {27, "Cathay Pacific", "Hong Kong", 3200000},
    {28, "Scoot", "Singapore", 1250000},
    {29, "Emirates", "Dubai", 6500000},
    {30, "Qatar Airways", "Doha", 7200000},
    {31, "Turkish Airlines", "Istanbul", 8000000},
    {32, "KLM Royal Dutch Airlines", "Amsterdam", 9000000},
    {33, "Lufthansa", "Frankfurt", 8500000},
    {34, "British Airways", "London", 9500000},
    {35, "Air France", "Paris", 8800000},
    {36, "Singapore Airlines", "Sydney", 10000000},
    {37, "Cathay Pacific", "New York", 12000000},
    {38, "Emirates", "Los Angeles", 11000000},
    {39, "Qatar Airways", "Toronto", 11500000},
    {40, "Turkish Airlines", "Dubai", 7000000}
};

const int SIZE = sizeof(tickets) / sizeof(tickets[0]);

string jsonEscape(const string& s) {
    string out;
    for (char c : s) {
        if (c == '"' || c == '\\') out += '\\';
        if (c == '\n') {
            out += "\\n";
        } else if (c == '\r') {
            out += "\\r";
        } else {
            out += c;
        }
    }
    return out;
}

string ticketJson(const Ticket& t) {
    return "{\"id\":" + to_string(t.id) +
           ",\"airline\":\"" + jsonEscape(t.airline) +
           "\",\"destination\":\"" + jsonEscape(t.destination) +
           "\",\"price\":" + to_string(t.price) + "}";
}

void bubbleSort(Ticket* data, int size, string& log) {
    log += "Bubble Sort: sorting by price (ascending)\\n";

    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            log += "Compare " + data[j].destination + " (Rp" +
                   to_string(data[j].price) + ") with " +
                   data[j + 1].destination + " (Rp" +
                   to_string(data[j + 1].price) + ")";

            if (data[j].price > data[j + 1].price) {
                Ticket temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
                log += " -> SWAP\\n";
            } else {
                log += " -> No swap\\n";
            }
        }
    }

    log += "Sorting complete.";
}

void linearSearch(Ticket* data, int size, string target,
                  string& log, int& foundIndex) {
    foundIndex = -1;
    log += "Linear Search: " + target + "\\n";

    string wanted = target;
    transform(wanted.begin(), wanted.end(), wanted.begin(),
              [](unsigned char c) { return tolower(c); });

    for (int i = 0; i < size; i++) {
        string current = data[i].destination;
        transform(current.begin(), current.end(), current.begin(),
                  [](unsigned char c) { return tolower(c); });

        log += "Step " + to_string(i + 1) + ": Check " +
               data[i].destination;

        if (current == wanted) {
            foundIndex = i;
            log += " -> MATCH FOUND\\n";
            return;
        }
        log += " -> No match\\n";
    }

    log += "No matching destination found.";
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cerr << "Usage: algorithms.exe sort | search DESTINATION\n";
        return 1;
    }

    string action = argv[1];
    Ticket data[SIZE];
    copy(tickets, tickets + SIZE, data);

    string log;
    int foundIndex = -1;

    if (action == "sort") {
        bubbleSort(data, SIZE, log);
    } else if (action == "search" && argc >= 3) {
        string target = argv[2];
        for (int i = 3; i < argc; i++) {
            target += " ";
            target += argv[i];
        }
        linearSearch(data, SIZE, target, log, foundIndex);
    } else {
        cerr << "Invalid action or missing destination.\n";
        return 1;
    }

    cout << "{\"tickets\":[";
    for (int i = 0; i < SIZE; i++) {
        if (i > 0) cout << ",";
        cout << ticketJson(data[i]);
    }
    cout << "],\"log\":\"" << jsonEscape(log)
         << "\",\"found_index\":" << foundIndex << "}\n";

    return 0;
}
