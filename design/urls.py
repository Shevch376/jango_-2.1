from django.urls import path, include

urlpatterns = [
    path('', include('mysite.urls')),  # Главная страница
    path('accounts/', include('django.contrib.auth.urls')),  # Вход и регистрация
]


