from django.http import HttpResponse
from django.template import loader

from planner.models import Task


def planner(request):
    return HttpResponse('<h1>Здесь будут отображаться дела</h1>')

def show_tasks(request):
    template = loader.get_template('planner/index.html')
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return HttpResponse(template.render(context, request))


