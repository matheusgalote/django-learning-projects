from django.urls import path
from . import views

urlpatterns = [
    path("", views.anime_rank, name="anime_rank"),
    path("<int:pk>", views.anime_detail, name="anime_detail")
]