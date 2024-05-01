from typing import Any, Dict

from fastapi import FastAPI
from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from interface.gateway.web.handlers.health_router import health_api
from starlette.responses import JSONResponse


class MainApplication(FastAPI):
    def __init__(self) -> None:
        # Prepare FastAPI Routes
        # Prepare FastAPI | ASGWI App Config
        _config: Dict[Any, Any] = dict()
        _config["debug"] = False
        _config["routes"] = None
        _config["title"] = "Uvicorn-FastAPI"
        _config["summary"] = None
        _config["description"] = "A simple FastAPI application using Uvicorn"
        _config["version"] = "0.1.0"
        _config["openapi_url"] = "/openapi.json"
        _config["openapi_tags"] = None
        _config["servers"] = None
        _config["dependencies"] = None
        _config["default_response_class"] = Default(JSONResponse)
        _config["redirect_slashes"] = True
        _config["docs_url"] = "/docs"
        _config["redoc_url"] = "/redoc"
        _config["swagger_ui_oauth2_redirect_url"] = "/docs/oauth2-redirect"
        _config["swagger_ui_init_oauth"] = None
        _config["middleware"] = None
        _config["exception_handlers"] = None
        _config["on_startup"] = None
        _config["on_shutdown"] = None
        _config["lifespan"] = None
        _config["on_shutdown"] = None
        _config["lifespan"] = None
        _config["terms_of_service"] = None
        _config["contact"] = None
        _config["license_info"] = None
        _config["openapi_prefix"] = ""
        _config["root_path"] = ""
        _config["root_path_in_servers"] = True
        _config["responses"] = None
        _config["callbacks"] = None
        _config["webhooks"] = None
        _config["deprecated"] = None
        _config["include_in_schema"] = True
        _config["swagger_ui_parameters"] = None
        _config["generate_unique_id_function"] = generate_unique_id
        _config["separate_input_output_schemas"] = True
        super().__init__(**_config)
        self.include_router(router=health_api)
