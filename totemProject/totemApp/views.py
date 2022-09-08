from django.http import HttpResponse
from django.shortcuts import render, redirect
from totemApp.models import *
from totemApp.forms import * 
from django.views.generic.base import TemplateView
 
class LandingPage(TemplateView):
    template_name = 'landing_page.html'



# Create your views here.
# To be optimized later:
# def createView(request):
#     addCountry = CountriesForm()
#     addKeyword = KeywordsForm()
#     addVertebrate = VertebratesForm()
#     addInvertebrate = InvertebratesForm()
#     forms = [addCountry, addKeyword, addVertebrate, addInvertebrate]
#     crud_widgets = ['c_r_u_dCountries', 'c_r_u_dKeywords', 'c_r_u_dVertebrates', 'c_r_u_dInvertebrates']
#     if request.method == 'POST':
#         for i in range(len(crud_widgets)):
#             if crud_widgets[i] in request.POST:
#                 for j in range(len(forms)):
#                     form = forms[j](request.POST)
#                     if form.is_valid():
#                         form.save()
#                         return redirect('createForms')
#     context = {
#         "addCountry": addCountry,
#         "addKeyword": addKeyword,
#         "addVertebrate": addVertebrate,
#         "addInvertebrate": addInvertebrate,
#     }
#     return render(request, 'create_view.html', context=context)


# "createEntry" is for adding to database tables
# Credit to Rafiq Hilali for this code @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
def createEntry(request):
    addCountry = CountriesForm()
    addKeyword = KeywordsForm()
    addVertebrate = VertebratesForm()
    addInvertebrate = InvertebratesForm()
    if request.method == 'POST':
        if 'c_r_u_dCountries' in request.POST:
            addCountry = CountriesForm(request.POST)
            if addCountry.is_valid():
                addCountry.save()
                return redirect('countryIndex')
        if 'c_r_u_dKeywords' in request.POST:
            addKeyword = KeywordsForm(request.POST)
            if addKeyword.is_valid():
                addKeyword.save()
                return redirect('keywordIndex')
        if 'c_r_u_dVertebrates' in request.POST:
            addVertebrate = VertebratesForm(request.POST)
            if addVertebrate.is_valid():
                addVertebrate.save()
                return redirect('vertebrateIndex')
        if 'c_r_u_dInvertebrates' in request.POST:
            addInvertebrate = InvertebratesForm(request.POST)
            if addInvertebrate.is_valid():
                addInvertebrate.save()
                return redirect('invertebrateIndex')
    context = {
        "addCountry": addCountry,
        "addKeyword": addKeyword,
        "addVertebrate": addVertebrate,
        "addInvertebrate": addInvertebrate,
    }
    return render(request, 'create_view.html', context=context)



# Countries index, update, & delete views
def countryIndex(request):
    countries = Countries.objects.all()
    return render(request, 'country_index_view.html', {'countries': countries})

def updateCountry(request, country_id):
    country_id = int(country_id)
    try:
        country = Countries.objects.get(id=country_id)
    except Countries.DoesNotExist:
        return redirect('countryIndex')
    countryForm = CountriesForm(request.POST or None, instance = country)
    if countryForm.is_valid():
        countryForm.save()
        return redirect ('countryIndex')
    return render(request, 'country_update_view.html', {'countryForm': countryForm})

def deleteCountry(request, country_id):
    country_id = int(country_id)
    try:
        country = Countries.objects.get(id=country_id)
    except Countries.DoesNotExist:
        return redirect('countryIndex')
    country.delete()
    return redirect('countryIndex')



# Keywords index, update, & delete views
def keywordIndex(request):
    keywords = Keywords.objects.all()
    return render(request, 'keyword_index_view.html', {'keywords': keywords})

def updateKeyword(request, keyword_id):
    keyword_id = int(keyword_id)
    try:
        keyword = Keywords.objects.get(id=keyword_id)
    except Keywords.DoesNotExist:
        return redirect('keywordIndex')
    keywordForm = KeywordsForm(request.POST or None, instance = keyword)
    if keywordForm.is_valid():
        keywordForm.save()
        return redirect ('keywordIndex')
    return render(request, 'keyword_update_view.html', {'keywordForm': keywordForm})

def deleteKeyword(request, keyword_id):
    keyword_id = int(keyword_id)
    try:
        keyword = Keywords.objects.get(id=keyword_id)
    except Keywords.DoesNotExist:
        return redirect('keywordIndex')
    keyword.delete()
    return redirect('keywordIndex')



# Vertebrates index, update, & delete views
def vertebrateIndex(request):
    vertebrates = Vertebrates.objects.all()
    return render(request, 'vertebrate_index_view.html', {'vertebrates': vertebrates})

def updateVertebrate(request, vertebrate_id):
    vertebrate_id = int(vertebrate_id)
    try:
        vertebrate = Vertebrates.objects.get(id=vertebrate_id)
    except Vertebrates.DoesNotExist:
        return redirect('vertebrateIndex')
    vertebrateForm = VertebratesForm(request.POST or None, instance = vertebrate)
    if vertebrateForm.is_valid():
        vertebrateForm.save()
        return redirect ('vertebrateIndex')
    return render(request, 'vertebrate_update_view.html', {'vertebrateForm': vertebrateForm})

def deleteVertebrate(request, vertebrate_id):
    vertebrate_id = int(vertebrate_id)
    try:
        vertebrate = Vertebrates.objects.get(id=vertebrate_id)
    except Vertebrates.DoesNotExist:
        return redirect('vertebrateIndex')
    vertebrate.delete()
    return redirect('vertebrateIndex')



# Invertebrates index, update, & delete views
def invertebrateIndex(request):
    invertebrates = Invertebrates.objects.all()
    return render(request, 'invertebrate_index_view.html', {'invertebrates': invertebrates})

def updateInvertebrate(request, invertebrate_id):
    invertebrate_id = int(invertebrate_id)
    try:
        invertebrate = Invertebrates.objects.get(id=invertebrate_id)
    except Invertebrates.DoesNotExist:
        return redirect('invertebrateIndex')
    invertebrateForm = InvertebratesForm(request.POST or None, instance = invertebrate)
    if invertebrateForm.is_valid():
        invertebrateForm.save()
        return redirect ('invertebrateIndex')
    return render(request, 'invertebrate_update_view.html', {'invertebrateForm': invertebrateForm})

def deleteInvertebrate(request, invertebrate_id):
    invertebrate_id = int(invertebrate_id)
    try:
        invertebrate = Invertebrates.objects.get(id=invertebrate_id)
    except Invertebrates.DoesNotExist:
        return redirect('invertebrateIndex')
    invertebrate.delete()
    return redirect('invertebrateIndex')
