import pytest
from flask import Flask


@pytest.fixture(autouse=True)
def app():
    return Flask(__name__)


@pytest.fixture(autouse=True)
def app_context(app):
    with app.test_request_context():
        yield
