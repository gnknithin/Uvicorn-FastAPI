from fastapi import status
from fastapi.routing import APIRouter
from interface.gateway.web.schemas.response_schemas import ResponseSchema

health_api = APIRouter(prefix="", tags=["system"])


@health_api.get(
    "/health",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
)
async def get_health() -> ResponseSchema:
    return ResponseSchema(status="Ok")
