from django.urls import path, include

from worker.views import login_view, register_worker

app_name = "worker"

urlpatterns = [
    path("login/", login_view, name="worker-login"),
    path("register/", register_worker, name="worker-register"),
]
