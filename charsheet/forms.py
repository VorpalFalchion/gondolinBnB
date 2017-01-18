from django import forms
from django.forms import inlineformset_factory
from .models import Character, Stats, Misc, Skills, Saves, Maneuvers, Attacks, Armor, Spells, Money, Gear, Feats, Links

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','race','char_class',]

class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['str','dex','con','int','wis','cha']

class MiscForm(forms.ModelForm):
    class Meta:
        model = Misc
        fields = ['hp','ac','flatfooted_ac','touch_ac','init','speed','damage_resistance']

#needs fixed -> many to one relationship with character
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_name','ranks']

SkillsFormSet = inlineformset_factory(Character, Skills, fields=['skill_name','ranks'])

class SavesForm(forms.ModelForm):
    class Meta:
        model = Saves
        fields = ['fort','reflex','will']

class ManeuversForm(forms.ModelForm):
    class Meta:
        model = Maneuvers
        fields = ['cmb','cmd']

#another many to one relationship
class AttacksForm(forms.ModelForm):
    class Meta:
        model = Attacks
        fields = ['attack_name','atk_bonus','crit','damage','range','type']

AttacksFormSet = inlineformset_factory(Character, Attacks, fields=['attack_name','atk_bonus','crit','damage','range','type'])

#many to one
class ArmorForm(forms.ModelForm):
    class Meta:
        model = Armor
        fields = ['armor_name','ac_bonus','max_dex','armor_penalty']

ArmorFormSet = inlineformset_factory(Character, Armor, fields=['armor_name','ac_bonus','max_dex','armor_penalty'])
#many to one
class SpellsForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ['spell_name','spell_desc','spell_lvl']

SpellsFormSet = inlineformset_factory(Character, Spells, fields=['spell_name','spell_lvl','spell_desc'])

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['gold','silver','copper']

#many to one
class GearForm(forms.ModelForm):
    class Meta:
        model = Gear
        fields = ['item_name','item_weight']

GearFormSet = inlineformset_factory(Character, Gear, fields=['item_name','item_weight'])

#many to one
class FeatsForm(forms.ModelForm):
    class Meta:
        model = Feats
        fields = ['feat_name','feat_desc']

FeatsFormSet = inlineformset_factory(Character, Feats, fields=['feat_name','feat_desc'])
#many to one
class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['link_name','link_url']

LinksFormSet = inlineformset_factory(Character, Links, fields=['link_name','link_url'])
