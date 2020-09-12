from django.urls import path
from . import views

urlpatterns = [
    path('login', views.logged_page),
    path('', views.index)
]