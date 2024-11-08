from django.urls import path
from . import views

app_name = "_tasks_app"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:task_id>/", views.task_detail, name='task'),
    path("add_task/", views.add_task, name='add_task'),
    path("update_status/<int:task_id>/", views.update_status, name='update_status'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path("delete/<int:task_id>/", views.delete_task, name='delete_task')
]