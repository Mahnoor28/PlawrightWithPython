from playwright.sync_api import sync_playwright

def test_api_delete():
    with sync_playwright() as p:
        request = p.request.new_context(
            extra_http_headers={"x-api-key": "reqres-free-v1"}
        )
        response = request.delete("https://reqres.in/api/users/2")
        assert response.status == 204  # No content
        print("DELETE status:", response.status)
        request.dispose()
        