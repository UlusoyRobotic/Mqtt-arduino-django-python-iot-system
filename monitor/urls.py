"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import post_view,home_view,database_view
from main.tests import get_data_computer
from main.tests2 import get_data_esp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',post_view,name='data_page' ),
    url(r'^database/',database_view ,name = 'database_page'),
    url(r'^data/computer/', get_data_computer),
    url(r'^data/esp/', get_data_esp),
    
]
