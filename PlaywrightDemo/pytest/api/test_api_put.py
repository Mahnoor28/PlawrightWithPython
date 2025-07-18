from playwright.sync_api import sync_playwright
def test_api_put():
    with sync_playwright() as p:
        request = p.request.new_context(
            extra_http_headers={"x-api-key": "reqres-free-v1"}
        )
        payload = {"name": "Alex", "job": "Senior QA"}
        response = request.put("https://reqres.in/api/users/2", data=payload)
        assert response.status == 200
        json_data = response.json()
        print(json_data)
        assert json_data["name"] == "Alex"
        assert json_data["job"] == "Senior QA"
        request.dispose()