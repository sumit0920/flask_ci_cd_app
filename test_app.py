import app

def test_homepage():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200

