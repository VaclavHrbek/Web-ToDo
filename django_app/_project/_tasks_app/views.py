from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import TaskForm

from .models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by('-created_at')[:5]
    context = {"latest_tasks_list": latest_tasks_list}
    return render(request, '_tasks_app/index.html', context)

def tasks(request):
    return render(request, '_tasks_app/tasks.html')

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at
    }
    return render(request, "_tasks_app/task.html", context)

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, '_tasks_app/tasks.html')
    else:
        form = TaskForm()
    return render(request, "_tasks_app/add_task.html", { "form": form })
