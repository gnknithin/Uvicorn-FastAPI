import uvicorn


def create_app():
    from fastapi import APIRouter, FastAPI, status
    from pydantic import BaseModel

    class HealthResponseModel(BaseModel):
        """Response Model to Validate and return when performing health check on API"""

        status: str

    health_router = APIRouter(
        prefix="",
        tags=["system"],
    )

    @health_router.get(
        "/health",
        response_model=HealthResponseModel,
        status_code=status.HTTP_200_OK,
        summary="Perform a Health Check",
        response_description="Return HTTP Status Code 200 (OK)",
    )
    async def get_health() -> HealthResponseModel:
        return HealthResponseModel(status="Ok")

    _initialized_app = FastAPI()
    _initialized_app.include_router(health_router)

    return _initialized_app


def run_main():
    import os

    _cpu_count: int = os.cpu_count() if os.cpu_count() is not None else 1
    _total_workers: int = (_cpu_count * 2) + 1
    # _main_awsgi_app = create_app()
    try:
        uvicorn.run(
            # app=_main_awsgi_app,
            app="main:create_app",
            host="127.0.0.1",
            port=8000,
            # loop="auto",
            workers=_total_workers,
            # reload=True,
            factory=True,
        )
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        print("Done")


if __name__ == "__main__":
    run_main()
