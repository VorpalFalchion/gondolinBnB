from django.shortcuts import render, redirect
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

def edit(request, id):
    character = Character.objects.get(pk=id)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)

        if form.is_valid():
            character = form.save(commit=False)
            character.player_id = request.user.id
            character.save()
            return redirect(index)

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
            return redirect(index)
    else:
        form = CharacterForm()
    return render(request, "charsheet/create.html", {'form': form,})

def delete(request, id):
    character = Character.objects.get(pk=id)

    character.delete()
    return redirect(index)
