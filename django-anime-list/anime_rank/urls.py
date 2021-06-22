from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.anime_rank, name="anime_rank")
]