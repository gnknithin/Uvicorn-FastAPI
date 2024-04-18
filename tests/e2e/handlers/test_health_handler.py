import pytest
from fastapi import status
from httpx import Response

from tests.base_tests import BaseE2ETest


class TestHealthHandler(BaseE2ETest):
    def test_should_check_health_handler_properly(self) -> None:
        # Arrange
        # Act
        _response: Response = self.client.get(url="/health")
        # Assert
        assert _response is not None
        assert _response.status_code == status.HTTP_200_OK
        assert _response.headers is not None
        assert "content-type" in _response.headers
        assert _response.headers["content-type"] == "application/json"

    @pytest.mark.asyncio
    async def test_should_check_health_handler_propert_for_async(self) -> None:
        # Arrange
        # Act
        _response: Response = await self.async_client.get(url="/health")
        # Assert
        assert _response is not None
        assert _response.status_code == status.HTTP_200_OK
        assert _response.headers is not None
        assert "content-type" in _response.headers
        assert _response.headers["content-type"] == "application/json"
