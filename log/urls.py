from django.urls import path, include

from log.views import index, BreakdownListView


app_name = "log"

urlpatterns = [
    path("", index, name="index"),
    path("logs/", BreakdownListView.as_view(), name="log-list")
]
