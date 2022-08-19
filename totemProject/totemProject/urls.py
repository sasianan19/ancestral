"""totemProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from totemApp.views import *  

urlpatterns = [
    path('admin/', admin.site.urls),

    # The following two paths, 'create' & 'update/delete', are for dev use only (for now)- site/app users should not be creating,
    # updating, or deleting anything in/from database tables 
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

    

]
