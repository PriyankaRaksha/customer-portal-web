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