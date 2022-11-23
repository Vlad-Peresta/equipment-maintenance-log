from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/task_list.html"
