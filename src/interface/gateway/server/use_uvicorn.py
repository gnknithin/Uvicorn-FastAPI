import os
import ssl
from typing import Any, Dict, Optional

from fastapi import FastAPI
from uvicorn.config import LOGGING_CONFIG, Config
from uvicorn.server import Server


class MainServer(Server):
    def __init__(self, initialized_app: FastAPI) -> None:
        _cpu_count: Optional[int] = os.cpu_count()
        _workers: int = ((_cpu_count if _cpu_count is not None else 1) * 2) + 1
        _config: Dict[Any, Any] = dict()
        _config["app"] = initialized_app
        _config["host"] = "127.0.0.1"
        _config["port"] = 8000
        _config["uds"] = None
        _config["fd"] = None
        _config["loop"] = "uvloop"
        _config["http"] = "h11"
        _config["ws"] = "auto"
        _config["ws_max_size"] = 16 * 1024 * 1024
        _config["ws_max_queue"] = 32
        _config["ws_ping_interval"] = 20.0
        _config["ws_ping_timeout"] = 20.0
        _config["ws_per_message_deflate"] = True
        _config["lifespan"] = "auto"
        _config["env_file"] = None
        _config["log_config"] = LOGGING_CONFIG
        _config["log_level"] = "info"
        _config["access_log"] = True
        _config["use_colors"] = True
        _config["interface"] = "auto"
        _config["reload"] = False
        _config["reload_dirs"] = None
        _config["reload_delay"] = 0.25
        _config["reload_includes"] = None
        _config["reload_excludes"] = None
        _config["workers"] = _workers
        _config["proxy_headers"] = True
        _config["server_header"] = True
        _config["date_header"] = True
        _config["forwarded_allow_ips"] = None
        _config["root_path"] = ""
        _config["limit_concurrency"] = None
        _config["limit_max_requests"] = None
        _config["backlog"] = 2048
        _config["timeout_keep_alive"] = 5
        _config["timeout_notify"] = 30
        _config["timeout_graceful_shutdown"] = None
        _config["callback_notify"] = None
        _config["ssl_keyfile"] = None
        _config["ssl_certfile"] = None
        _config["ssl_keyfile_password"] = None
        _config["ssl_version"] = ssl.PROTOCOL_TLS_SERVER
        _config["ssl_cert_reqs"] = ssl.CERT_NONE
        _config["ssl_ca_certs"] = None
        _config["ssl_ciphers"] = "TLSv1"
        _config["headers"] = None
        _config["factory"] = False
        _config["h11_max_incomplete_event_size"] = None

        _server_config = Config(**_config)

        super().__init__(config=_server_config)
        # Setup Event Loop
        self.config.setup_event_loop()
