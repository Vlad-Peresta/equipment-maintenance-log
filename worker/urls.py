from django.contrib.auth.views import LogoutView
from django.urls import path, include

from worker.views import login_view, register_worker, WorkerListView

app_name = "worker"

urlpatterns = [
    path("accounts/login/", login_view, name="worker-login"),
    path("accounts/logout/", LogoutView.as_view(), name="worker-logout"),
    path("accounts/register/", register_worker, name="worker-register"),
    path("workers/", WorkerListView.as_view(), name="worker-list")
]
