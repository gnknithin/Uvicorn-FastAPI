from pydantic import BaseModel


class ResponseSchema(BaseModel):
    """Response Model to Validate and return when performing health check on API"""

    status: str
