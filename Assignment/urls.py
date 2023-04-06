from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("userview/", views.userview),
    path("logindata/", views.logindata)
]
