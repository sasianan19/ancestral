from django.shortcuts import render, redirect
from totemApp.models import *
from totemApp.forms import * 

# Create your views here.

# "create_view" is for adding to database tables
# Credit to Rafiq Hilali for this code @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
def create_view(request):
    addCountry = CountriesForm()
    addKeyword = KeywordsForm()
    addVertebrate = VertebratesForm()
    addInvertebrate = InvertebratesForm()
    if request.method == 'POST':
        if 'c_r_u_dCountries' in request.POST:
            addCountry = CountriesForm(request.POST)
            if addCountry.is_valid():
                addCountry.save()
                return redirect('createForms')
        if 'c_r_u_dKeywords' in request.POST:
            addKeyword = KeywordsForm(request.POST)
            if addKeyword.is_valid():
                addKeyword.save()
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
        "addKeyword": addKeyword,
        "addVertebrate": addVertebrate,
        "addInvertebrate": addInvertebrate,
    }
    return render(request, 'create_view.html', context=context)



def country_list_view(request):
    countries = Countries.objects.all()
   
    return render(request, 'country_list_view.html', {'countries': countries})

def vertebrate_list_view(request):
    vertebrates = Vertebrates.objects.all()
   
    return render(request, 'vertebrate_list_view.html', {'vertebrates': vertebrates})

def invertebrate_list_view(request):
    invertebrates = Invertebrates.objects.all()
   
    return render(request, 'invertebrate_list_view.html', {'invertebrates': invertebrates})

def keyword_list_view(request):
    keywords = Keywords.objects.all()
   
    return render(request, 'keyword_list_view.html', {'keywords': keywords})