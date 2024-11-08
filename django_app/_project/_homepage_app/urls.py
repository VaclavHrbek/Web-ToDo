from django.urls import path
from . import views

app_name = "_homepage_app"
urlpatterns = [
    path("", views.index, name='index'),
]