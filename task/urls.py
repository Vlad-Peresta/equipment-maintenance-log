from django.urls import path

from task.views import TaskListView, TaskTypeListView, TaskTypeUpdateView, TaskTypeDeleteView, TaskTypeCreateView

app_name = "task"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task_types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task_types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
]
