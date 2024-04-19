from locust import FastHttpUser, HttpUser, constant, task

"""
[WIP]
[tool.locust]
locustfile = "tests/load"
host = "127.0.0.1:8000"
users = 10
spawn-rate = 1
run-time = "2s"
web-host = "127.0.0.1"
web-port = 8089
headless= false
autostart = false
loglevel = "INFO"
autoquit = -1
master = false
web-login= false
legacy-ui = false
tags = ["Documentation","Health","System"]
class-picker = false
"""


# locust -f tests/load/test_health_handler.py -u 10000 -r 1000 -t 1m
class TestSwaggerHandlerAPI(HttpUser):
    wait_time = constant(1)
    host = "http://127.0.0.1:8000"

    @task
    def check(self):
        _ = self.client.get("/docs")


class TestHealthHandlerAPI(FastHttpUser):
    wait_time = constant(1)
    host = "http://127.0.0.1:8000"

    @task
    def check(self):
        with self.rest(method="GET", url="/health") as _resp:
            pass
