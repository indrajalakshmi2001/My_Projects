from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),  # Define the route for the home view
    path("login",views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path("details",views.details, name="details")
    
    
]
