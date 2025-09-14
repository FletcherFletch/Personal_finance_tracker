from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
import json


User = get_user_model()

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None 

        try:

            user = User.objects.create_user(username, password=password, email=email)  
            user.save()

            return redirect("login")
        
        except Exception as e:
            print(f"Error: {e}")

    return render(request, "Auth/register.html", {})

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if all ([username, password]):
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
        
    return render(request, "Auth/login.html", {})

def home_view(request):
    
    if request.method == 'POST':

        username = request.POST.get("username")


    return render(request, "Home/home.html", {})

def dashboard_view(request):
    labels = ['rent', 'Food', 'Transport', 'Entertainment', 'Savings']
    data = [1200, 500, 150, 200, 300]

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data), 
    }
        
    return render(request, "Home/dashboard.html", context)
    
