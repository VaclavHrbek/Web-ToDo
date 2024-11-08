from django.urls import path
from . import views

app_name = "_tasks_app"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:task_id>/", views.task_detail, name='task'),
    path("add_task/", views.add_task, name='add_task'),
]