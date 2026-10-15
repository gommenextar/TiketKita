
const ticketGrid = document.getElementById("ticketGrid");
const statusElement = document.getElementById("status");
const logElement = document.getElementById("log");
const searchForm = document.getElementById("searchForm");
const destinationInput = document.getElementById("destination");
const resultsHeading = document.getElementById("resultsHeading");
const resultsSubtitle = document.getElementById("resultsSubtitle");
const sortButton = document.getElementById("sortButton");
const toggleLogButton = document.getElementById("toggleLog");
const logContainer = document.getElementById("logContainer");
const toggleLogLabel = document.getElementById("toggleLogLabel");

function formatPrice(price) {
    return "Rp" + price.toLocaleString("id-ID");
}

function renderTickets(tickets) {
    ticketGrid.replaceChildren();

    if (tickets.length === 0) {
        const empty = document.createElement("div");
        empty.className = "empty-state";

        const icon = document.createElement("div");
        icon.className = "empty-icon";
        icon.textContent = "⌕";

        const heading = document.createElement("h3");
        heading.textContent = "No tickets found";

        const message = document.createElement("p");
        message.textContent =
            "Try another destination, such as Bali or Surabaya.";

        empty.append(icon, heading, message);
        ticketGrid.appendChild(empty);
        return;
    }

    tickets.forEach(ticket => {
        const card = document.createElement("article");
        card.className = "ticket-card";

        const top = document.createElement("div");
        top.className = "ticket-top";

        const airline = document.createElement("div");
        airline.className = "airline";

        const icon = document.createElement("div");
        icon.className = "airline-icon";
        icon.textContent = "✈";

        const airlineName = document.createElement("span");
        airlineName.textContent = ticket.airline;

        airline.append(icon, airlineName);

        const ticketId = document.createElement("span");
        ticketId.className = "ticket-id";
        ticketId.textContent =
            "TKT-" + String(ticket.id).padStart(3, "0");

        top.append(airline, ticketId);

        const route = document.createElement("div");
        route.className = "route";

        const destination = document.createElement("div");

        const label = document.createElement("div");
        label.className = "destination-label";
        label.textContent = "YOUR DESTINATION";

        const name = document.createElement("div");
        name.className = "destination-name";
        name.textContent = ticket.destination;

        destination.append(label, name);

        const line = document.createElement("div");
        line.className = "route-line";

        const plane = document.createElement("span");
        plane.textContent = "✈";
        line.appendChild(plane);

        route.append(destination, line);

        const bottom = document.createElement("div");
        bottom.className = "ticket-bottom";

        const priceBlock = document.createElement("div");

        const priceLabel = document.createElement("div");
        priceLabel.className = "price-label";
        priceLabel.textContent = "Ticket price";

        const price = document.createElement("div");
        price.className = "price";
        price.textContent = formatPrice(ticket.price);

        const unit = document.createElement("span");
        unit.className = "price-unit";
        unit.textContent = " / ticket";

        price.appendChild(unit);
        priceBlock.append(priceLabel, price);

        const bookingButton = document.createElement("button");
        bookingButton.className = "booking-button";
        bookingButton.type = "button";
        bookingButton.textContent = "Select ticket";

        bookingButton.addEventListener("click", () => {
            alert(
                "You selected " + ticket.airline +
                " to " + ticket.destination +
                " for " + formatPrice(ticket.price) +
                ". Booking is a demo feature for now."
            );
        });

        bottom.append(priceBlock, bookingButton);
        card.append(top, route, bottom);
        ticketGrid.appendChild(card);
    });
}

async function runAlgorithm(action) {
    const destination = destinationInput.value.trim();
    const params = new URLSearchParams({ action });

    if (action === "search") {
        if (!destination) {
            resultsHeading.textContent = "Explore destinations";
            resultsSubtitle.textContent =
                "Enter a destination to find a ticket.";
            statusElement.textContent =
                "Please enter a destination first.";
            destinationInput.focus();
            return;
        }

        params.set("destination", destination);

        resultsHeading.textContent = "Search results";
        resultsSubtitle.textContent =
            `Showing tickets matching "${destination}".`;
    } else {
        resultsHeading.textContent = "Explore destinations";
        resultsSubtitle.textContent =
            "Tickets sorted from cheapest to most expensive.";
    }

    ticketGrid.setAttribute("aria-busy", "true");

    const loading = document.createElement("div");
    loading.className = "empty-state";

    const heading = document.createElement("h3");
    heading.textContent = "Loading tickets...";

    loading.appendChild(heading);
    ticketGrid.replaceChildren(loading);
    statusElement.textContent = "";

    try {
        const response = await fetch(
            `/api/tickets/?${params.toString()}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.error || "Unable to load tickets."
            );
        }

        let displayedTickets = data.tickets;

        if (action === "search") {
            displayedTickets = data.found_index >= 0
                ? [data.tickets[data.found_index]]
                : [];
        }

        renderTickets(displayedTickets);
        logElement.textContent = data.log;

        statusElement.textContent =
            `${displayedTickets.length} ticket(s) displayed.`;

        sortButton.textContent = action === "sort"
            ? "✓ Sorted by cheapest"
            : "↕ Sort: Cheapest first";
    } catch (error) {
        ticketGrid.replaceChildren();

        const message = document.createElement("div");
        message.className = "empty-state";

        const heading = document.createElement("h3");
        heading.textContent = "Unable to load tickets";

        const description = document.createElement("p");
        description.textContent =
            "Check that the Django server and C++ executable are available.";

        message.append(heading, description);
        ticketGrid.appendChild(message);

        statusElement.textContent = error.message;
    } finally {
        ticketGrid.setAttribute("aria-busy", "false");
    }
}

searchForm.addEventListener("submit", event => {
    event.preventDefault();
    runAlgorithm("search");
});

sortButton.addEventListener("click", () => {
    runAlgorithm("sort");
});

toggleLogButton.addEventListener("click", () => {
    logContainer.hidden = !logContainer.hidden;

    const isOpen = !logContainer.hidden;

    toggleLogButton.setAttribute(
        "aria-expanded",
        String(isOpen)
    );

    toggleLogLabel.textContent = isOpen
        ? "Hide algorithm log −"
        : "Show algorithm log ＋";
});

// Load all tickets in price order when the page opens.
runAlgorithm("sort");
