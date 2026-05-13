def test_dashboard_response():
    response = client.get("/dashboard")

    assert response.status_code == 200