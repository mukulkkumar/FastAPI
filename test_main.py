from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_greet():
    response = client.get("/hello/Alice")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Alice!"}

def test_create_item():
    data = {"name": "Book", "price": 12.5, "is_offer": True}
    response = client.post("/items/", json=data)
    assert response.status_code == 200
    assert response.json() == {"item": data}

def test_create_item_default_is_offer():
    data = {"name": "Pen", "price": 2.0}
    response = client.post("/items/", json=data)
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Pen", "price": 2.0, "is_offer": False}}

def test_upload_file():
    file_content = b"Hello, file!"
    files = {"file": ("test.txt", file_content, "text/plain")}
    response = client.post("/uploadfile/", files=files)
    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["filename"] == "test.txt"
    assert json_resp["content_type"] == "text/plain"
    assert json_resp["size"] == len(file_content)

