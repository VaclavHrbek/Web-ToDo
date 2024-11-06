from django.urls import path
from . import views

app_name = "_tasks_app"
urlpatterns = [
    path("", views.index, name='index'),
    path("tasks/", views.tasks, name='tasks'),
    path("tasks/<int:task_id>/", views.task, name='task')
]