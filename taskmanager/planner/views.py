from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from planner.models import Task


def planner(request):
    return HttpResponse('<h1>Здесь будут отображаться дела</h1>')

def show_tasks(request):
    template = loader.get_template('planner/index.html')
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return HttpResponse(template.render(context, request))

def by_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    context = {'tasks': tasks}
    return render(request, 'planner/index.html', context)



