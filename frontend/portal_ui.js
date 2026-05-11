function renderDashboard(data) {
    document.getElementById("portal").innerHTML = `
        <h2>Welcome ${data.user.name}</h2>
        <p>Total Orders: ${data.orders.length}</p>
    `;
}