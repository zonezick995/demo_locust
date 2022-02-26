from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)
    host = "https://postman-echo.com"

    @task
    def index_page(self):
        self.client.get("/get?foo1=bar1&foo2=bar2")