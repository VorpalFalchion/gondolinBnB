from django.shortcuts import render


# Create your views here.
def sheet(request):
    return render(request, 'charsheet/sheet.html')

def index(request):

    return render(request, 'charsheet/index.html')

def edit(request):
    return render(request, 'charsheet/edit.html')
