from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm
# Create your views here.
@login_required(login_url="login/")

def home(request):
    return render(request, "clientcolony/home.html")

def logout_view(request):
    logout(request)
    return redirect(request, 'login')

def new_user(request):
    form = UserForm()
    return render(request, "clientcolony/new_user.html", {'form': form})
