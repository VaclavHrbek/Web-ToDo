from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task

# Create your views here.

def index(request):
    latest_tasks_list = Task.objects.order_by('-created_at')[:5]
    context = {"latest_tasks_list": latest_tasks_list}
    return render(request, 'index.html', context)

def tasks(request):
    return render(request, 'tasks.html')

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at
    }
    return render(request, "task.html", context)
