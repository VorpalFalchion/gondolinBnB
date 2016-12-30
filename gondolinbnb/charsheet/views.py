from django.shortcuts import render


# Create your views here.
def sheet(request):
    return render(request, 'charsheet/sheet.html')
