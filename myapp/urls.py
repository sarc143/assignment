from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manager/<int:manager_id>/', views.manager_employees, name='manager_employees'),
]
