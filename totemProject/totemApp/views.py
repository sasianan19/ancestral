from django.shortcuts import render, redirect
from totemApp.models import *
from totemApp.forms import * 

# Create your views here.

# "create_view" is for adding to database tables
# Credit to Rafiq Hilali for this code @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
def create_view(request):
    addCountry = CountriesForm()
    addVertebrate = VertebratesForm()
    addInvertebrate = InvertebratesForm()
    if request.method == 'POST':
        if 'c_r_u_dCountries' in request.POST:
            addCountry = CountriesForm(request.POST)
            if addCountry.is_valid():
                addCountry.save()
                return redirect('createForms')
        if 'c_r_u_dVertebrates' in request.POST:
            addVertebrate = VertebratesForm(request.POST)
            if addVertebrate.is_valid():
                addVertebrate.save()
                return redirect('createForms')
        if 'c_r_u_dInvertebrates' in request.POST:
            addInvertebrate = InvertebratesForm(request.POST)
            if addInvertebrate.is_valid():
                addInvertebrate.save()
                return redirect('createForms')
    context = {
        "addCountry": addCountry,
        "addVertebrate": addVertebrate,
        "addInvertebrate": addInvertebrate,
    }
    return render(request, 'create_view.html', context=context)

