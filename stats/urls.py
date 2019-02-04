from django.urls import path
from . import views

urlpatterns = [
    path('statistics', views.execute_list, name='execute_list'),
]
