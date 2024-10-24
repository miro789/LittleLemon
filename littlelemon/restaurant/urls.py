from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu_list, name="menu-list"),
    path("booking/", views.booking, name="booking")
]
