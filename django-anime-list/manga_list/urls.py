from django.urls import path 
from . import views

urlpatterns = [
    path("", views.manga_index, name="manga_index"),
    path("<int:pk>", views.manga_detail, name="manga_detail")
]