import asyncio

from fastapi import FastAPI
from interface.gateway.server.use_uvicorn import MainServer
from interface.gateway.web.app.use_fastapi import MainApplication


async def run_main_new():
    # Create FastAPI | ASGWI App
    _asgi_app: FastAPI = MainApplication()
    # Create Uvicorn Server passing ASGWI App Type in the background
    _server_uvicorn = MainServer(initialized_app=_asgi_app)
    try:
        # Workers need to to be spinned up
        _ = await _server_uvicorn.serve()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    try:
        _ = await _server_uvicorn.shutdown()
    except asyncio.exceptions.CancelledError:
        print("Handler asyncio.exceptions.CancelledError")
        pass

    print("Done")


if __name__ == "__main__":
    asyncio.run(run_main_new())
