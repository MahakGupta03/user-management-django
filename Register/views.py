from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        return HttpResponse("done")
    return render(request,"register.html")

def user_login(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request,user_obj)
            return HttpResponse("done")
    return render(request,"login.html")

