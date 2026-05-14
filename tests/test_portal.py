def test_dashboard_response():
    response = client.get("/dashboard")

    assert response.status_code == 200

def test_empty_order_dashboard():
    response = client.get("/dashboard/empty")

    assert response.status_code == 200