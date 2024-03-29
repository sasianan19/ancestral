from django.shortcuts import (render, 
                              redirect)
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
    context_object_name = 'data'

    template_name='search_results_page.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        myset = {
            'animalsList': list(chain(
            Vertebrates.objects.filter(
                Q(animal__icontains=query) | Q(classification__classification__icontains=query) |
                Q(country__country__icontains=query)),
            Invertebrates.objects.filter(
                Q(animal__icontains=query) | Q(classification__classification__icontains=query) |
                Q(country__country__icontains=query)),
            )),
            'animalsKeywords': list(chain(
                Vertebrates.objects.filter(Q(keywords__keyword__icontains=query)),
                Invertebrates.objects.filter(Q(keywords__keyword__icontains=query))
            )),
            'countries': Countries.objects.filter(country__icontains=query),
            'class': AnimalClass.objects.filter(classification__icontains=query),
            'animalNames': list(chain(
                Vertebrates.objects.filter(animal__icontains=query),
                Invertebrates.objects.filter(animal__icontains=query)
            )),
            'keywordsList': Keywords.objects.filter(keyword__icontains=query)
        }

        return myset
    
# AFRICA PAGE
class AfricaPage(ListView):
    template_name = 'africa_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='2').all(),
            Invertebrates.objects.filter(country__continent='2').all(),
        ))
        countries = Countries.objects.filter(continent='2').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'africa_tab.html', context)

# ANTARCTICA PAGE
class AntarcticaPage(ListView):
    template_name = 'antarctica_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='5').all(),
            Invertebrates.objects.filter(country__continent='5').all()
        ))
        countries = Countries.objects.filter(continent='5').order_by('country')

        context = {
        'content': content, 
        'countries': countries
        }

        return render(request, 'antarctica_tab.html', context)

# ASIA PAGE
class AsiaPage(ListView):
    template_name = 'asia_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='1').all(),
            Invertebrates.objects.filter(country__continent='1').all()
        ))
        countries = Countries.objects.filter(continent='1').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'asia_tab.html', context)

# AUSTRALIA/OCEANIA PAGE
class Aus_OceaniaPage(ListView):
    template_name = 'aus-oceania_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='7').all(),
            Invertebrates.objects.filter(country__continent='7').all()
        ))
        countries = Countries.objects.filter(continent='7').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'aus-oceania_tab.html', context)

# EUROPE PAGE
class EuropePage(ListView):
    template_name = 'europe_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='6').all(),
            Invertebrates.objects.filter(country__continent='6').all()
        ))
        countries = Countries.objects.filter(continent='6').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'europe_tab.html', context)

# NORTH AMERICA PAGE
class NorthAmericaPage(ListView):
    template_name = 'north-america_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='3').all(),
            Invertebrates.objects.filter(country__continent='3').all()
        ))
        countries = Countries.objects.filter(continent='3').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'north-america_tab.html', context)

# SOUTH AMERICA PAGE
class SouthAmericaPage(ListView):
    template_name = 'south-america_tab.html'

    def get(self, request):
        content = list(chain(
            Vertebrates.objects.filter(country__continent='4').all(),
            Invertebrates.objects.filter(country__continent='4').all()
        ))
        countries = Countries.objects.filter(continent='4').order_by('country')

        context = {
        'content': content,
        'countries': countries
        }

        return render(request, 'south-america_tab.html', context)
    
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
