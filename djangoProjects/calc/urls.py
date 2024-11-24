from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the route for the home view
    path('add', views.add, name='add')
]

