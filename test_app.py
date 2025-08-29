import werkzeug
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "patched"

from app import app  # import after patch

def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
