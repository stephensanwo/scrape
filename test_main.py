from fastapi.testclient import TestClient
import json
from main import api

client = TestClient(api)

data = {
    "url": "http://httpbin.org/post",
    "headers": {
        "header-1": "value-1"
    },
    "cookies": {
        "cookie_key": "cookie_value"

    },
    "payload": {
        "key1": "value1",
        "key2": "value2"

    }
}
url = "http://httpbin.org"


def test_root():
    response = client.get("/test")
    assert response.status_code == 200


def test_scrape_get():
    response = client.get("/scrape", params={"url": url})
    assert response.status_code == 200


def test_scrape_post():
    response = client.post("/scrape", json=data)

    # Test that the url returns the correct status code
    assert response.status_code == 200

    response_body = json.loads(response.json())

    # Test that the custom headers were added to the request
    assert response_body["headers"]["Header-1"] == "value-1"

    # Test that payload was present in the request
    assert response_body["json"]["key1"] == "value1"

    # Test that the custom cookies were added to the request
    assert response_body['headers']["Cookie"] == "cookie_key=cookie_value"
