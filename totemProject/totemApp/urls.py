from django.urls import path
from totemApp.views import *


urlpatterns = [
    #------- dev URLs -------#
    path('create', createEntry),

    path('countries', countryIndex, name='countryIndex'),
    path('updateCountry/<pk>', updateCountry),
    path('deleteCountry/<pk>', deleteCountry),

    path('keywords', keywordIndex, name='keywordIndex'),
    path('updateKeyword/<pk>', updateKeyword),
    path('deleteKeyword/<pk>', deleteKeyword),

    path('vertebrates', vertebrateIndex, name='vertebrateIndex'),
    path('updateVertebrate/<pk>', updateVertebrate),
    path('deleteVertebrate/<pk>', deleteVertebrate),

    path('invertebrates', invertebrateIndex, name='invertebrateIndex'),
    path('updateInvertebrate/<pk>', updateInvertebrate),
    path('deleteInvertebrate/<pk>', deleteInvertebrate),

    #------- user URLs -------#
    path('ancestral/', LandingPage.as_view(), name='landingPage'),
    path('home/', HomePage.as_view(), name='homePage'),
    path('search/', SearchResultsPage.as_view(), name='results'),
    path('africa', AfricaPage.as_view(), name='africa'),
    
]