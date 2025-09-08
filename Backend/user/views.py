from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


User = get_user_model()

def register_view(request):

    if request.method == 'POST':
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None 

        try:

            user = User.objects.create_user(username, password=password, email=email)  
            user.save()

        except Exception as e:
            print(f"Error: {e}")

    return render(request, "Auth/register.html", {})
    
