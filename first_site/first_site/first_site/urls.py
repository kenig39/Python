from django.urls import path
from first_site import views

urlpatterns = [
    path("", views.home),
    path("index/", views.index),
    path("catalog/", views.catalog),
]

