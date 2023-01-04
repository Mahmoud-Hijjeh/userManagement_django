from django.shortcuts import render
# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
def dashboard(request):
    return render(request, "users/dashboard.html")
# new
def register(request):
   if request.method == "GET":
      return render(request, "users/register.html",{"form": CustomUserCreationForm})
   elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))