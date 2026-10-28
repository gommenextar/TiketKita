const mode = document.body.dataset.mode;
const ticketGrid = document.getElementById("ticketGrid");
const statusElement = document.getElementById("status");
const logElement = document.getElementById("log");
const searchForm = document.getElementById("searchForm");
const originInput = document.getElementById("origin");
const destinationInput = document.getElementById("destination");
const providerInput = document.getElementById("provider");
const resetSearchButton = document.getElementById("resetSearch");
const resultsHeading = document.getElementById("resultsHeading");
const resultsSubtitle = document.getElementById("resultsSubtitle");
const sortButton = document.getElementById("sortButton");
const sortOrder = document.getElementById("sortOrder");
const toggleLogButton = document.getElementById("toggleLog");
const logContainer = document.getElementById("logContainer");
const toggleLogLabel = document.getElementById("toggleLogLabel");
const categoryNames = {
    flight: "flights",
    train: "trains",
    ship: "ships",
    hotel: "hotels",
};
const icons = { flight: "✈", train: "🚆", ship: "⛴", hotel: "⌂" };
const sortDescriptions = {
    price: "lowest price",
    duration: "shortest duration",
    departure: "earliest departure time",
};

function formatPrice(price) {
    return "Rp" + price.toLocaleString("id-ID");
}

function addText(parent, tag, className, value) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = value;
    parent.appendChild(element);
    return element;
}

function arrivalDaySuffix(departure, duration) {
    const [departureHours, departureMinutes] = departure.split(":").map(Number);
    const durationParts = duration.matchAll(/(\d+)(d|h|m)/g);
    let durationMinutes = 0;
    for (const [, value, unit] of durationParts) {
        const amount = Number(value);
        durationMinutes += unit === "d" ? amount * 1440 : unit === "h" ? amount * 60 : amount;
    }
    const arrivalDay = Math.floor(
        (departureHours * 60 + departureMinutes + durationMinutes) / 1440
    );
    return arrivalDay ? ` +${arrivalDay}` : "";
}

function renderTickets(tickets) {
    ticketGrid.replaceChildren();

    if (tickets.length === 0) {
        const column = document.createElement("div");
        column.className = "col-12";
        const empty = document.createElement("div");
        empty.className = "empty-state card border-0 shadow-sm";
        const emptyBody = document.createElement("div");
        emptyBody.className = "card-body text-center py-5";
        addText(emptyBody, "div", "empty-icon", "⌕");
        addText(emptyBody, "h3", "h5", "No options found");
        addText(
            emptyBody,
            "p",
            "text-secondary mb-0",
            "Try a different origin, destination, or provider."
        );
        empty.appendChild(emptyBody);
        column.appendChild(empty);
        ticketGrid.appendChild(column);
        return;
    }

    tickets.forEach(ticket => {
        const column = document.createElement("div");
        column.className = "col-12 col-xl-6";
        const card = document.createElement("article");
        card.className = "card ticket-card h-100 shadow-sm";
        const cardBody = document.createElement("div");
        cardBody.className = "card-body d-flex flex-column p-4";

        const top = document.createElement("div");
        top.className = "ticket-top";
        const provider = document.createElement("div");
        provider.className = "airline";
        addText(provider, "div", "airline-icon", icons[mode]);
        addText(
            provider,
            "span",
            "",
            mode === "flight"
                ? `${ticket.provider} / ${ticket.number}`
                : ticket.provider
        );
        if (mode === "hotel") {
            addText(top, "span", "ticket-id", `${ticket.rating}-star stay`);
        } else if (mode !== "flight") {
            const serviceLabel = mode === "train"
                ? `Train ${ticket.number}`
                : ticket.number;
            addText(
                top,
                "span",
                "ticket-id",
                serviceLabel
            );
        }
        top.prepend(provider);

        const route = document.createElement("div");
        route.className = "route";
        const origin = document.createElement("div");
        if (mode !== "hotel") {
            addText(origin, "div", "destination-label", "FROM");
            addText(origin, "div", "destination-name", ticket.origin);
            if (ticket.origin_code) {
                addText(origin, "div", "location-code", ticket.origin_code);
            }
            addText(origin, "span", "route-time", ticket.departure);
        }

        const destination = document.createElement("div");
        addText(
            destination,
            "div",
            "destination-label",
            mode === "hotel" ? "STAY IN" : "TO"
        );
        addText(destination, "div", "destination-name", ticket.destination);
        if (ticket.destination_code) {
            addText(destination, "div", "location-code", ticket.destination_code);
        }
        if (mode !== "hotel") {
            addText(
                destination,
                "span",
                "route-time",
                `${ticket.arrival}${arrivalDaySuffix(ticket.departure, ticket.duration)}`
            );
        }
        if (mode === "hotel") {
            route.append(destination);
        } else {
            const routeMiddle = document.createElement("div");
            routeMiddle.className = "route-middle";
            addText(routeMiddle, "div", "route-duration", ticket.duration);
            const line = document.createElement("div");
            line.className = "route-line";
            addText(line, "span", "", icons[mode]);
            routeMiddle.appendChild(line);
            route.append(origin, routeMiddle, destination);
        }

        const schedule = document.createElement("div");
        schedule.className = "schedule";
        if (mode === "hotel") {
            addText(schedule, "div", "schedule-item", `Check-in ${ticket.check_in}`);
            addText(schedule, "div", "schedule-item", `Check-out ${ticket.check_out}`);
            addText(schedule, "div", "schedule-item", ticket.duration);
        }

        const bottom = document.createElement("div");
        bottom.className = "ticket-bottom";
        const priceBlock = document.createElement("div");
        addText(priceBlock, "div", "price-label", mode === "hotel" ? "Price / night" : "Ticket price");
        const price = addText(priceBlock, "div", "price", formatPrice(ticket.price));
        addText(price, "span", "price-unit", mode === "hotel" ? " / night" : " / ticket");

        const bookingButton = document.createElement("button");
        bookingButton.className = "btn btn-primary booking-button";
        bookingButton.type = "button";
        bookingButton.textContent = "Select";
        bookingButton.addEventListener("click", () => {
            if (mode !== "hotel") {
                window.location.href = `/trips/${mode}/${ticket.id}/`;
                return;
            }
            alert(
                `You selected ${ticket.provider} to ${ticket.destination} ` +
                `for ${formatPrice(ticket.price)}. Booking is a demo feature.`
            );
        });

        bottom.appendChild(priceBlock);
        bottom.appendChild(bookingButton);
        cardBody.append(top, route);
        if (mode === "hotel") cardBody.appendChild(schedule);
        cardBody.appendChild(bottom);
        card.appendChild(cardBody);
        column.appendChild(card);
        ticketGrid.appendChild(column);
    });
}

async function runAlgorithm(action) {
    const origin = originInput ? originInput.value.trim() : "";
    const destination = destinationInput.value.trim();
    const provider = providerInput.value.trim();
    const params = new URLSearchParams({ action, mode });
    const selectedSort = sortOrder ? sortOrder.value : "price";
    params.set("sort_by", selectedSort);
    const sortDescription = sortDescriptions[selectedSort];
    const filters = [];
    if (origin) {
        params.set("origin", origin);
        filters.push(`origin "${origin}"`);
    }
    if (destination) {
        params.set("destination", destination);
        filters.push(`destination "${destination}"`);
    }
    if (provider) {
        params.set("provider", provider);
        filters.push(`provider "${provider}"`);
    }

    if (action === "search" && filters.length === 0) {
        resultsSubtitle.textContent = "Enter a search term to find options.";
        statusElement.textContent = "Please enter an origin, destination, or provider first.";
        destinationInput.focus();
        return;
    }

    resultsHeading.textContent = filters.length
        ? `${action === "sort" ? "Sorted " : ""}Search results`
        : `Explore ${categoryNames[mode]}`;
    resultsSubtitle.textContent = filters.length
        ? `Showing ${categoryNames[mode]} for ${filters.join(" and ")}${action === "sort" ? `, sorted by ${sortDescription}.` : `, ordered by ${sortDescription}.`}`
        : action === "sort"
            ? `${categoryNames[mode][0].toUpperCase()}${categoryNames[mode].slice(1)} sorted by ${sortDescription}.`
            : "Find an option that matches your budget.";

    ticketGrid.setAttribute("aria-busy", "true");
    const loading = document.createElement("div");
    loading.className = "empty-state";
    addText(loading, "h3", "", "Loading options...");
    ticketGrid.replaceChildren(loading);
    statusElement.textContent = "";

    try {
        const response = await fetch(`/api/tickets/?${params.toString()}`);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || "Unable to load options.");
        }
        const displayedTickets = filters.length
            ? data.matching_indices.map(index => data.tickets[index])
            : data.tickets;
        renderTickets(displayedTickets);
        logElement.textContent = data.log;
        statusElement.textContent = `${displayedTickets.length} option(s) displayed.`;
        if (sortButton) {
            sortButton.textContent = action === "sort"
                ? "✓ Sorted by cheapest"
                : "↕ Sort: Cheapest first";
        }
    } catch (error) {
        ticketGrid.replaceChildren();
        const message = document.createElement("div");
        message.className = "empty-state";
        addText(message, "h3", "", "Unable to load options");
        addText(message, "p", "", "Check that the Django server is available.");
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

resetSearchButton.addEventListener("click", () => {
    searchForm.reset();
    runAlgorithm("sort");
});

if (sortButton) {
    sortButton.addEventListener("click", () => runAlgorithm("sort"));
}
if (sortOrder) {
    sortOrder.addEventListener("change", () => runAlgorithm("sort"));
}

toggleLogButton.addEventListener("click", () => {
    logContainer.hidden = !logContainer.hidden;
    const isOpen = !logContainer.hidden;
    toggleLogButton.setAttribute("aria-expanded", String(isOpen));
    toggleLogLabel.textContent = isOpen
        ? "Hide algorithm log −"
        : "Show algorithm log ＋";
});

runAlgorithm("sort");
