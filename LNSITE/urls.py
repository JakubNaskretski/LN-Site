"""LNSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from appone import views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

# favicon_view = RedirectView.as_view(url='/static/appone/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^$', views.StronaGlowna, name='StronaGlowna'),
    path('admin/', admin.site.urls),
    path('appone/',include('appone.urls')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'))

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
