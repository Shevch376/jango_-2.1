from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('my_requests/', views.my_all_requests, name='my_all_requests'),  # Мои заявки
    path('create_request/', views.create_request, name='create_request'),  # Создание заявки
    path('signup/', views.logins, name='logins'),  # Регистрация
    path('requests/delete/<int:pk>/', views.delete_request, name='delete_request'),  # Удаление заявки
    path('profile/', views.profile, name='profile'),  # Профиль пользователя
    path('requests/change_status/<int:pk>/', views.change_request_status, name='change_request_status'),  # Изменение статуса заявки
]
