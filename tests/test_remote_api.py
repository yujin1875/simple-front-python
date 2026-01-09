import requests

def test_remote_get_posts(base_url):
    """
    외부 API(jsonplaceholder) GET 테스트
    """
    url = f"{base_url}/posts/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["id"] == 1
