from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, WorkerUpdateForm
from .models import Worker


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("worker:worker-list"))
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})


def register_worker(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            success = True

            return redirect(reverse_lazy("log:index"))

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "worker/worker_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "worker/worker_detail.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("worker:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("worker:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("worker:worker-list")
    template_name = "worker/worker_detail.html"

