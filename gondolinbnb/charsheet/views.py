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

def edit(request, id=''):
    new_flag = False
    character = ''
    if id=='':
        new_flag = True
    else:
        character = Character.objects.get(pk=id)

    if request.method == "POST":
        form = CharacterForm(request.POST)

        if form.is_valid() and new_flag == True:
            new_char = form.save(commit=False)
            new_char.player_id = request.user.id
            new_char.save()
        elif form.is_valid() and new_flag == False:
            character.save()

    else:
        if new_flag == True:
            form = CharacterForm()
        else:
            form = CharacterForm(instance=character)

    context = {
        'character': character,
        'form': form,
    }
    return render(request, "charsheet/edit.html", context)

def create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_char = form.save(commit=False)
            new_char.player_id = request.user.id
            new_char.save()
    else:
        form = CharacterForm()
    return render(request, "charsheet/create.html", {'form': form,})
