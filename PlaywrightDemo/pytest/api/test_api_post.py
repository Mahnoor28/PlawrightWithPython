from playwright.sync_api import sync_playwright

def test_api_post():
    with sync_playwright() as p:
        request = p.request.new_context(
            extra_http_headers={"x-api-key": "reqres-free-v1"}
        )
        payload = {"name": "Alex", "job": "QA Engineer"}
        response = request.post("https://reqres.in/api/users", data=payload)
        assert response.status == 201
        json_data = response.json()
        print(json_data)
        assert json_data["name"] == "Alex"
        assert json_data["job"] == "QA Engineer"
        request.dispose()