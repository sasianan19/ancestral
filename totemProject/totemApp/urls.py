from django.urls import path
from totemApp.views import *

urlpatterns = [
    path('create', createEntry),

    path('countries', countryIndex, name='countryIndex'),
    path('updateCountry/<country_id>', updateCountry),
    path('deleteCountry/<country_id>', deleteCountry),

    path('keywords', keywordIndex, name='keywordIndex'),
    path('updateKeyword/<keyword_id>', updateKeyword),
    path('deleteKeyword/<keyword_id>', deleteKeyword),

    path('vertebrates', vertebrateIndex, name='vertebrateIndex'),
    path('updateVertebrate/<vertebrate_id>', updateVertebrate),
    path('deleteVertebrate/<vertebrate_id>', deleteVertebrate),

    path('invertebrates', invertebrateIndex, name='invertebrateIndex'),
    path('updateInvertebrate/<invertebrate_id>', updateInvertebrate),
    path('deleteInvertebrate/<invertebrate_id>', deleteInvertebrate),

    #------- user URLs -------#
    path('totem/', LandingPage.as_view(), name='landingPage'),
]