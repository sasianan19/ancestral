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
    path('antarctica', AntarcticaPage.as_view(), name='antarctica'),
    path('asia', AsiaPage.as_view(), name='asia'),
    path('australia-oceania', Aus_OceaniaPage.as_view(), name='aus-oceania'),
    path('europe', EuropePage.as_view(), name='europe'),
    path('north-america', NorthAmericaPage.as_view(), name='north-america'),
    path('south-america', SouthAmericaPage.as_view(), name='south-america')
    
]