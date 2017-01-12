from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
@login_required(login_url="login/")

def home(request):
    return render(request, "clientcolony/home.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def new_user(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        form = UserForm(request.POST)
        if form.is_valid():
            new_user = user_form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            login(request, new_user)
            registered = True
    else:
        form = UserForm()
    return render(request, "clientcolony/new_user.html", {'form': form, 'registered': registered})
