from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from .models import PieChart
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

    #global labels_list, data_list  

   
    
    if request.method == "POST":
        form_name = request.POST.get("form_name")
        # value = request.POST.get("value")
        # rent = request.POST.get("rent")
        # transport = request.POST.get("transport")
        # food = request.POST.get("food")
        # entertainment = request.POST.get("entertainment")

        #labels = request.POST.get("label")

            #when forms are submitted, django sees
            #request.POST = { 'csrfmiddlewaretoken':'csrfcode', 'rent': '1200',}
            #django takes the form as a dictionary with a key and a value 
            #value always prints a string, even numbers it comes out as "1200" need float(value) to get 1200
        if form_name == "category1":
            #for key, value in request.POST.items():
            label = request.POST.get("category")
                #if key == 'csrfmiddlewaretoken':
                    #continue
            if label:
                try:
                    PieChart.objects.update_or_create(
                        label= label.capitalize(),
                        #default={'amount': 0}
                        amount = 0
                    )
                except ValueError:
                    pass
        if form_name == "delete_category":
            name = request.POST.get("")
            
        if form_name == "amount_spent":
            for key, value in request.POST.items():
                #^ this loops through that dictionary 
                #.items() dictionary method to get (key,value) pairs 
                if key == 'csrfmiddlewaretoken':
                    continue
                #checkst hat csrf token is there and skips it 
                try:
                    amount = float(value)
                    PieChart.objects.update_or_create(
                        label = key.capitalize(), 
                        defaults={'amount': amount}
                    )
                except ValueError:
                    continue
            #This grabs data to render chart 
    piechart = PieChart.objects.all()
    labels = [entry.label for entry in piechart]
    data = [float(entry.amount) for entry in piechart]

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data), 
        'categories': piechart
    }
        
    return render(request, "Home/dashboard.html", context)
    
