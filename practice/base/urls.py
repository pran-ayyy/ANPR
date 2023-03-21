from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('vehicle/<str:pk>/', views.vehiclePage, name='vehicle'),
    path('create-vehicle/<str:s>/', views.createVehicle, name='create-vehicle'),
    path('logs/', views.logsPage, name='logs'),
    path('create-log/', views.createLog, name='create-log'),
    path('intro/', views.introPage, name='intro'),
]