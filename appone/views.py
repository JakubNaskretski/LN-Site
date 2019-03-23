from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# TODO: Make somehow autoupdating views


# Create your views here.
def StronaGlowna(request):
    return render(request, "appone/StronaGlowna.html")

def Uslugi(request):
    return render(request, "appone/Uslugi.html")

def GotoweRozwiazania(request):
    funcdrinksprod = Product.objects.filter(product_type='Napoje funkcjonalne')
    #TODO: czy filtr może się jakoś automatycznie aktualizowac?
    syrupprod = Product.objects.filter(product_type='Syropy')
    return render(request, "appone/GotoweRozwiazania.html", {'funcdrinksprod':funcdrinksprod, 'syrupprod':syrupprod})

def Blog(request):
    return render(request, "appone/Blog.html")

def ONas(request):
    return render(request, "appone/ONas.html")

def Kontakt(request):
    return render(request, "appone/Kontakt.html")
