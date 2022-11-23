from django.urls import path, include

from log.views import index, LogListView


app_name = "log"

urlpatterns = [
    path("", index, name="index"),
    path("logs/", LogListView.as_view(), name="log-list")
]
