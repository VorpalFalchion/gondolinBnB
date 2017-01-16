from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CharacterForm
from .models import Character

@login_required(login_url='login/')

# Create your views here.
def sheet(request, id):
    character = Character.objects.get(pk=id)
    context = {
        'character': character,
    }
    return render(request, 'charsheet/sheet.html', context)

def index(request):
    character_list = Character.objects.filter(player_id=request.user.id)
    context = {
        'character_list': character_list,
    }
    return render(request, 'charsheet/index.html', context)

def edit(request):
    registered = False

    if request.method == "POST":
        #character_form = CharacterForm(data=request.POST)
        #character_form.player_id = request.user

        form = CharacterForm(request.POST)
        #form.player_id = request.user

        if form.is_valid():
            new_char = form.save(commit=False)
            new_char.player_id = request.user.id
            new_char.save()
            registered = True
    else:
        form = CharacterForm()
    return render(request, "charsheet/edit.html", {'form': form, 'registered': registered})
