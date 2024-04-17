from abc import ABC

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from main import create_app


class BaseE2ETest(ABC):
    pytestmark: pytest.MarkDecorator = pytest.mark.e2e

    def get_app(self) -> FastAPI:
        return create_app()

    @property
    def client(self) -> TestClient:
        return TestClient(app=self.get_app())

    @property
    def async_client(self):
        _transport = ASGITransport(app=self.get_app())
        return AsyncClient(transport=_transport, base_url="http://testserver")
