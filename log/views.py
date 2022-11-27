from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from log.models import Breakdown, Equipment
from task.models import Task
from worker.models import Worker


@login_required
def index(request):
    staff_amount = Worker.objects.count()
    equipment_amount = Equipment.objects.count()
    active_tasks_amount = Task.objects.filter(is_completed=False).count()
    active_failures_amount = Breakdown.objects.filter(status="process").count()

    context = {
        # 'segment': 'index',
        "staff_amount": staff_amount,
        "equipment_amount": equipment_amount,
        "active_tasks_amount": active_tasks_amount,
        "active_failures_amount": active_failures_amount,
    }

    return render(request, "home/index.html", context=context)



def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class BreakdownListView(generic.ListView):
    model = Breakdown
    template_name = "log/log_list.html"
