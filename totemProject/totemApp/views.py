from django.shortcuts import render, redirect
from totemApp.models import *
from totemApp.forms import * 

# Create your views here.

# "create_view" is for adding to database tables
# Credit to Rafiq Hilali for this code @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
def createView(request):
    addCountry = CountriesForm()
    addKeyword = KeywordsForm()
    addVertebrate = VertebratesForm()
    addInvertebrate = InvertebratesForm()
    if request.method == 'POST':
        if 'c_r_u_dCountries' in request.POST:
            addCountry = CountriesForm(request.POST)
            if addCountry.is_valid():
                addCountry.save()
                return redirect('countryList')
        if 'c_r_u_dKeywords' in request.POST:
            addKeyword = KeywordsForm(request.POST)
            if addKeyword.is_valid():
                addKeyword.save()
                return redirect('keywordList')
        if 'c_r_u_dVertebrates' in request.POST:
            addVertebrate = VertebratesForm(request.POST)
            if addVertebrate.is_valid():
                addVertebrate.save()
                return redirect('vertebrateList')
        if 'c_r_u_dInvertebrates' in request.POST:
            addInvertebrate = InvertebratesForm(request.POST)
            if addInvertebrate.is_valid():
                addInvertebrate.save()
                return redirect('invertebrateList')
    context = {
        "addCountry": addCountry,
        "addKeyword": addKeyword,
        "addVertebrate": addVertebrate,
        "addInvertebrate": addInvertebrate,
    }
    return render(request, 'create_view.html', context=context)



# Countries list, detail, update, & delete views
def countryListView(request):
    countries = Countries.objects.all()
    return render(request, 'country_list_view.html', {'countries': countries})

def countryDetailView(request, id):
    country = Countries.objects.get(id=id)
    return render(request, 'country_detail_view.html', {'country': country})




# Keywords list, detail, update, & delete views
def keywordListView(request):
    keywords = Keywords.objects.all()
    return render(request, 'keyword_list_view.html', {'keywords': keywords})

def keywordDetailView(request, id):
    keyword = Keywords.objects.get(id=id)
    return render(request, 'keyword_detail_view.html', {'keyword': keyword})



# Vertebrates list, detail, update, & delete views
def vertebrateListView(request):
    vertebrates = Vertebrates.objects.all()
    return render(request, 'vertebrate_list_view.html', {'vertebrates': vertebrates})

def vertebrateDetailView(request, id):
    vertebrate = Vertebrates.objects.get(id=id)
    vertebrates = Vertebrates.objects.all()
    return render(request, 'vertebrate_detail_view.html', {'vertebrate': vertebrate, 'vertebrates': vertebrates})



# Invertebrates list, detail, update, & delete views
def invertebrateListView(request):
    invertebrates = Invertebrates.objects.all()
    return render(request, 'invertebrate_list_view.html', {'invertebrates': invertebrates})

def invertebrateDetailView(request, id):
    invertebrate = Invertebrates.objects.get(id=id)
    invertebrates = Invertebrates.objects.all()
    return render(request, 'invertebrate_detail_view.html', {'invertebrate': invertebrate, 'invertebrates': invertebrates})

