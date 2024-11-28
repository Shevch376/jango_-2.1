from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RequestForm

def home(request):
    return render(request, 'home.html')  # Главная страница без дополнительных данных

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # или другая страница после входа
    return render(request, 'registration/login.html')

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.user = request.user  # Привязываем заявку к пользователю
            request_instance.save()
            return redirect('my_requests')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def my_requests(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'my_requests.html', {'requests': requests})

@login_required
def delete_request(request, pk):
    request_obj = get_object_or_404(Request, pk=pk, user=request.user)
    if request.method == 'POST':
        request_obj.delete()
        return redirect('my_requests')
    return render(request, 'delete_request.html', {'request': request_obj})
