from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_requests/', views.my_all_requests, name='my_all_requests'),
    path('create_request/', views.create_request, name='create-request'),
    path('signup/', views.logins, name='logins'),
    path('requests/delete/<int:pk>/', views.delete_request, name='delete_request'),
    path('categories/', views.manage_categories, name='manage_categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('profile/', views.profile, name='profile'),
    path('requests/change_status/<int:pk>/', views.change_request_status, name='change_request_status'),
    path('requests/', views.manage_requests, name='manage_requests'),
]
