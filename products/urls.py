from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('tasks/<int:id>/', views.task_detail, name="details"),
]
