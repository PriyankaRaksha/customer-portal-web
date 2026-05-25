function renderDashboard(data) {
    if (!data.orders || data.orders.length === 0) {
        document.getElementById("portal").innerHTML = `
            <p>No orders found</p>
        `;
        return;
    }

    document.getElementById("portal").innerHTML = `
        <h2>${data.user.name}</h2>
    `;
}

function renderPayments(data) {
    document.getElementById("payments").innerHTML =
        `<p>Total Payments: ${data.length}</p>`;
}