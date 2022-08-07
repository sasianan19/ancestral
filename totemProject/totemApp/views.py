from django.shortcuts import render
from totemApp.models import *
from totemApp.forms import * 

# Create your views here.
def addCountry(request):
    if request.method == "POST":
        form = CountriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CountriesForm()
    return render(request, 'db-forms.html', {'CountriesForm': form})


def addVertebrate(request):
    if request.method == "POST":
        form = VertebratesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VertebratesForm()
    return render(request, 'db-forms.html', {'VertebratesForm': form})


def addInvertebrate(request):
    if request.method == "POST":
        form = InvertebratesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InvertebratesForm()
    return render(request, 'db-forms.html', {'InvertebratesForm': form})