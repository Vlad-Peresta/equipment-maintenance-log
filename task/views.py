from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from task.forms import TaskTypeForm
from task.models import Task, TaskType


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task/task_list.html"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task/task_type_form.html"
    success_url = reverse_lazy("task:task-type-list")
    form_class = TaskTypeForm


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task/task_type_form.html"
    success_url = reverse_lazy("task:task-type-list")
    context_object_name = "task_type"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task/task_type_form.html"
    success_url = reverse_lazy("task:task-type-list")
    context_object_name = "task_type"
