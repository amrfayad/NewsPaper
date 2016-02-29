"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
<<<<<<< HEAD
    #url(r'^sections$', views.sections),
    url(r'^sections/(?P<section_name>[A-Za-z]+)', views.post),
    url(r'^sections/(?P<post_id>[0-9]+)', views.showpost),

=======
    url(r'^sections$', views.sections),
    url(r'^sections/(?P<section_name>[a-z]+)', views.post),
    url(r'^register/$',views.register),
     url(r'^home',views.home),


    url(r'^login$', auth.login), #You Must Override registration templates

    url(r'^logout$',views.logout_page),
    
>>>>>>> 09e252fd8a15d2b54b070e1f1dbb0d8589b34d37
    url(r'^page$', views.pagination),
  
]
