from django.urls import path 
from . import views

urlpatterns = [
    path("", views.manga_index, name="manga_index"),
]