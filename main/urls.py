from django.urls import path
from . import views

urlpatterns = [
    path('', views.flights_view, name='flights'),
    path('login/', views.login_view, name='login'),
    path('flights/', views.flights_view, name='flights'),
    path('uavs/', views.uavs_view, name='uavs'),
    path('maintenance/', views.flights_view, name='maintenance'),
    path('settings/', views.settings_view, name='settings'),
    path('logout/', views.logout_view, name='logout'),
]
