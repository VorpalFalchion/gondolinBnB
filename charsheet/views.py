from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CharacterForm, StatsForm, MiscForm, SkillsForm, SavesForm, ManeuversForm, AttacksForm, ArmorForm, SpellsForm, MoneyForm, GearForm, FeatsForm, LinksForm, SkillsFormSet, AttacksFormSet, ArmorFormSet, SpellsFormSet, GearFormSet, FeatsFormSet, LinksFormSet
from .models import Character, Stats, Misc, Skills, Saves, Maneuvers, Attacks, Armor, Spells, Money, Gear, Feats, Links

@login_required(login_url='login/')

# Create your views here.
def sheet(request, id):
    character = Character.objects.get(pk=id)
    stats = Stats.objects.get(belongs_to=character)
    misc = Misc.objects.get(belongs_to=character)
    skills = Skills.objects.filter(belongs_to=character)
    saves = Saves.objects.get(belongs_to=character)
    maneuvers = Maneuvers.objects.get(belongs_to=character)
    attacks = Attacks.objects.filter(belongs_to=character)
    armor = Armor.objects.filter(belongs_to=character)
    spells = Spells.objects.filter(belongs_to=character)
    money = Money.objects.get(belongs_to=character)
    gear = Gear.objects.filter(belongs_to=character)
    feats = Feats.objects.filter(belongs_to=character)
    links = Links.objects.filter(belongs_to=character)

    context = {
        'character': character,
        'stats': stats,
        'misc': misc,
        'skills': skills,
        'saves': saves,
        'maneuvers': maneuvers,
        'attacks': attacks,
        'armor': armor,
        'spells': spells,
        'money': money,
        'gear': gear,
        'feats': feats,
        'links': links,
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
    misc = Misc.objects.get(belongs_to=character)
    #skills = Skills.objects.filter(belongs_to=character)
    saves = Saves.objects.get(belongs_to=character)
    maneuvers = Maneuvers.objects.get(belongs_to=character)
    money = Money.objects.get(belongs_to=character)

    if request.method == "POST":
        character_form = CharacterForm(request.POST, instance=character)
        stats_form = StatsForm(request.POST, instance=stats)
        misc_form = MiscForm(request.POST, instance=misc)
        skills_formset = SkillsFormSet(request.POST, instance=character)
        saves_form = SavesForm(request.POST, instance=saves)
        maneuvers_form = ManeuversForm(request.POST, instance=maneuvers)
        attacks_formset = AttacksFormSet(request.POST, instance=character)
        armor_formset = ArmorFormSet(request.POST, instance=character)
        spells_formset = SpellsFormSet(request.POST, instance=character)
        money_form = MoneyForm(request.POST, instance=money)
        gear_formset = GearFormSet(request.POST, instance=character)
        feats_formset = FeatsFormSet(request.POST, instance=character)
        links_formset = LinksFormSet(request.POST, instance=character)

        validate = False

        if character_form.is_valid() and stats_form.is_valid() and misc_form.is_valid() and skills_formset.is_valid() and saves_form.is_valid() and maneuvers_form.is_valid() and attacks_formset.is_valid() and armor_formset.is_valid() and spells_formset.is_valid() and money_form.is_valid() and gear_formset.is_valid and feats_formset.is_valid() and links_formset.is_valid():
            validate = True
        if validate:
            character.save()
            stats.save()
            misc.save()
            skills_formset.save()
            saves_form.save()
            maneuvers_form.save()
            attacks_formset.save()
            armor_formset.save()
            spells_formset.save()
            money_form.save()
            gear_formset.save()
            feats_formset.save()
            links_formset.save()

            return redirect(index)

    character_form = CharacterForm(instance=character)
    stats_form = StatsForm(instance=stats)
    misc_form = MiscForm(instance=misc)
    skills_formset = SkillsFormSet(instance=character)
    saves_form = SavesForm(instance=saves)
    maneuvers_form = ManeuversForm(instance=maneuvers)
    attacks_formset = AttacksFormSet(instance=character)
    armor_formset = ArmorFormSet(instance=character)
    spells_formset = SpellsFormSet(instance=character)
    money_form = MoneyForm(instance=money)
    gear_formset = GearFormSet(instance=character)
    feats_formset = FeatsFormSet(instance=character)
    links_formset = LinksFormSet(instance=character)

    context = {
        'character': character,
        'character_form': character_form,
        'stats': stats,
        'stats_form': stats_form,
        'misc': misc,
        'misc_form': misc_form,
        'skills_formset': skills_formset,
        'saves': saves,
        'saves_form': saves_form,
        'maneuvers': maneuvers,
        'maneuvers_form': maneuvers_form,
        'attacks_formset': attacks_formset,
        'armor_formset': armor_formset,
        'spells_formset': spells_formset,
        'money': money,
        'money_form': money_form,
        'gear_formset': gear_formset,
        'feats_formset': feats_formset,
        'links_formset': links_formset,
    }
    return render(request, "charsheet/edit.html", context)

def create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        stats_form = StatsForm()
        misc_form = MiscForm()
        skills_form = SkillsForm()
        saves_form = SavesForm()
        maneuvers_form = ManeuversForm()
        attacks_form = AttacksForm()
        armor_form = ArmorForm()
        spells_form = SpellsForm()
        money_form = MoneyForm()
        gear_form = GearForm()
        feats_form = FeatsForm()
        links_form = LinksForm()

        if form.is_valid():
            new_char = form.save(commit=False)
            new_char.player_id = request.user.id
            new_char.save()

            new_stats = stats_form.save(commit=False)
            new_stats.belongs_to = new_char
            new_stats.save()

            new_misc = misc_form.save(commit=False)
            new_misc.belongs_to = new_char
            new_misc.save()

            new_skills = skills_form.save(commit=False)
            new_skills.belongs_to = new_char
            new_skills.save()

            new_saves = saves_form.save(commit=False)
            new_saves.belongs_to = new_char
            new_saves.save()

            new_maneuvers = maneuvers_form.save(commit=False)
            new_maneuvers.belongs_to = new_char
            new_maneuvers.save()

            new_attacks = attacks_form.save(commit=False)
            new_attacks.belongs_to = new_char
            new_attacks.save()

            new_armor = armor_form.save(commit=False)
            new_armor.belongs_to = new_char
            new_armor.save()

            new_spells = spells_form.save(commit=False)
            new_spells.belongs_to = new_char
            new_spells.save()

            new_money = money_form.save(commit=False)
            new_money.belongs_to = new_char
            new_money.save()

            new_gear = gear_form.save(commit=False)
            new_gear.belongs_to = new_char
            new_gear.save()

            new_feats = feats_form.save(commit=False)
            new_feats.belongs_to = new_char
            new_feats.save()

            new_links = links_form.save(commit=False)
            new_links.belongs_to = new_char
            new_links.save()

            return redirect(index)
    else:
        form = CharacterForm()
    return render(request, "charsheet/create.html", {'form': form,})

def delete(request, id):
    character = Character.objects.get(pk=id)

    character.delete()
    return redirect(index)
