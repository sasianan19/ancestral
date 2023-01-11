from django.shortcuts import (render, 
                              redirect,
                              get_object_or_404,
                              HttpResponseRedirect)
from totemApp.models import *
from totemApp.forms import * 
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from itertools import chain
 

# LANDING PAGE
class LandingPage(TemplateView):
    template_name = 'index.html'

# HOME PAGE
class HomePage(TemplateView):
    template_name='home_page.html'

# SEARCH RESULTS PAGE
class SearchResultsPage(ListView):
    template_name='search_results_page.html'

    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = list(chain(
            Vertebrates.objects.filter(
                Q(animal__icontains=query)),
            Invertebrates.objects.filter(
                Q(animal__icontains=query))
            )
        )
           
        return object_list
    

    


# "createEntry" is for adding to database tables
# Credit to Rafiq Hilali @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
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

def updateCountry(request, pk):
    country = Countries.objects.get(id=pk)
    form = CountriesForm(instance=country)

    if request.method == 'POST':
        form = CountriesForm(request.POST, instance = country)
        if form.is_valid():
            form.save()
            return redirect('countryIndex')

    context = {
        'country': country, 
        'form': form
    }

    return render(request, 'country_update_view.html', context)

def deleteCountry(request, pk):
    country = Countries.objects.get(id=pk)

    if request.method == 'POST':
        country.delete()
        return redirect('countryIndex')

    context = {
        'country': country
    }

    return render(request, 'country_delete_view.html', context)


# Keywords index, update, & delete views
def keywordIndex(request):
    keywords = Keywords.objects.all()
    return render(request, 'keyword_index_view.html', {'keywords': keywords})

def updateKeyword(request, pk):
    keyword = Keywords.objects.get(id=pk)
    form = KeywordsForm(instance=keyword)

    if request.method == 'POST':
        form = KeywordsForm(request.POST, instance = keyword)
        if form.is_valid():
            form.save()
            return redirect('keywordIndex')

    context = {
        'keyword': keyword, 
        'form': form
    }
    
    return render(request, 'keyword_update_view.html', context)

def deleteKeyword(request, pk):
    keyword = Keywords.objects.get(id=pk)

    if request.method == 'POST':
        keyword.delete()
        return redirect('keywordIndex')

    context = {
        'keyword': keyword
    }

    return render(request, 'keyword_delete_view.html', context)



# Vertebrates index, update, & delete views
def vertebrateIndex(request):
    vertebrates = Vertebrates.objects.all()
    return render(request, 'vertebrate_index_view.html', {'vertebrates': vertebrates})

def updateVertebrate(request, pk):
    vertebrate = Vertebrates.objects.get(id=pk)
    form = VertebratesForm(instance=vertebrate)

    if request.method == 'POST':
        form = VertebratesForm(request.POST, instance = vertebrate)
        if form.is_valid():
            form.save()
            return redirect('vertebrateIndex')

    context = {
        'vertebrate': vertebrate, 
        'form': form
    }
    
    return render(request, 'vertebrate_update_view.html', context)

def deleteVertebrate(request, pk):
    vertebrate = Vertebrates.objects.get(id=pk)

    if request.method == 'POST':
        vertebrate.delete()
        return redirect('vertebrateIndex')

    context = {
        'vertebrate': vertebrate
    }

    return render(request, 'vertebrate_delete_view.html', context)



# Invertebrates index, update, & delete views
def invertebrateIndex(request):
    invertebrates = Invertebrates.objects.all()
    return render(request, 'invertebrate_index_view.html', {'invertebrates': invertebrates})

def updateInvertebrate(request, pk):
    invertebrate = Invertebrates.objects.get(id=pk)
    form = InvertebratesForm(instance=invertebrate)

    if request.method == 'POST':
        form = InvertebratesForm(request.POST, instance = invertebrate)
        if form.is_valid():
            form.save()
            return redirect('invertebrateIndex')

    context = {
        'invertebrate': invertebrate, 
        'form': form
    }
    
    return render(request, 'invertebrate_update_view.html', context)

def deleteInvertebrate(request, pk):
    invertebrate = Invertebrates.objects.get(id=pk)

    if request.method == 'POST':
        invertebrate.delete()
        return redirect('invertebrateIndex')

    context = {
        'invertebrate': invertebrate
    }

    return render(request, 'invertebrate_delete_view.html', context)
