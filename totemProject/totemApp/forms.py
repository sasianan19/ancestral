from django import forms
from totemApp.models import *

# The following two forms are commented out because they were only used to add a SET number of
# continents (7) and classifications (11). 
# class ContinentsForm(forms.ModelForm):
#     class Meta:
#         model = Continents 
#         fields = ['continent']
#         labels = {'continent': "Continent"}

# class AnimalClassForm(forms.ModelForm):
#     class Meta:
#         model = AnimalClass
#         fields = ['classification']
#         labels = {'classification': "Classification"} 


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ['country', 'continent']
        labels = {'country': "Country", 'continent': "Continent"}

class VertebratesForm(forms.ModelForm):
    class Meta:
        model = Vertebrates
        fields = ['classification', 'animal', 'country', 'meaning']
        labels = {'classification': "Class", 'animal': "Animal", 'country': "Country", 'meaning': "Meaning"}

class InvertebratesForm(forms.ModelForm):
    class Meta:
        model = Invertebrates
        fields = ['classification', 'animal', 'country', 'meaning']
        labels = {'classification': "Class", 'animal': "Animal", 'country': "Country", 'meaning': "Meaning"}