
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
    {1, "Garuda Indonesia", "Jakarta", 1200000},
    {2, "Lion Air", "Bali", 650000},
    {3, "Citilink", "Surabaya", 800000},
    {4, "Batik Air", "Yogyakarta", 950000}
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
