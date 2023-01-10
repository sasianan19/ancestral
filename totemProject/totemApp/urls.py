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
    path('updateVertebrate/<vertebrate_id>', updateVertebrate),
    path('deleteVertebrate/<vertebrate_id>', deleteVertebrate),

    path('invertebrates', invertebrateIndex, name='invertebrateIndex'),
    path('updateInvertebrate/<invertebrate_id>', updateInvertebrate),
    path('deleteInvertebrate/<invertebrate_id>', deleteInvertebrate),

    #------- user URLs -------#
    path('ancestral/', LandingPage.as_view(), name='landingPage'),
    path('home/', HomePage.as_view(), name='homePage'),
    path('results/', SearchResultsPage.as_view(), name='results'),
]