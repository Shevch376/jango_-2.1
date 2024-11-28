from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('create_request/', views.create_request, name='create_request'),
]
