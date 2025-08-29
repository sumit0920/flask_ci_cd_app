import werkzeug
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "3.x"  # dummy version to satisfy Flask test_client

from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
