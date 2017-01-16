from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CharacterForm, StatsForm
from .models import Character, Stats

@login_required(login_url='login/')

# Create your views here.
def sheet(request, id):
    character = Character.objects.get(pk=id)
    stats = Stats.objects.get(belongs_to=character)

    context = {
        'character': character,
        'stats': stats,
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
    stats = Stats.objects.get(belongs_to=character)
    if request.method == "POST":
        character_form = CharacterForm(request.POST, instance=character)
        stats_form = StatsForm(request.POST, instance=stats)

        if character_form.is_valid() and stats_form.is_valid():
            #character = form.save(commit=False)
            #character.player_id = request.user.id
            character.save()
            stats.save()

            return redirect(index)

    character_form = CharacterForm(instance=character)
    stats_form = StatsForm(instance=stats)

    context = {
        'character': character,
        'character_form': character_form,
        'stats': stats,
        'stats_form': stats_form,
    }
    return render(request, "charsheet/edit.html", context)

def create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        stats_form = StatsForm()
        if form.is_valid():
            new_char = form.save(commit=False)
            new_char.player_id = request.user.id
            new_char.save()
            new_stats = stats_form.save(commit=False)
            new_stats.belongs_to = new_char
            new_stats.save()
            return redirect(index)
    else:
        form = CharacterForm()
    return render(request, "charsheet/create.html", {'form': form,})

def delete(request, id):
    character = Character.objects.get(pk=id)

    character.delete()
    return redirect(index)
