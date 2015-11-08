from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout, authenticate, login as login_user

from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect('/users/login')
        
    else:
        return render(request, 'register.html')
        
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            login_user(request, user)
            return HttpResponseRedirect('/profiles')
            
    else:
        return render (request, 'login.html')
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/users/login')
    