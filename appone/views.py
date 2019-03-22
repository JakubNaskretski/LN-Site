from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def StronaGlowna(request):
    return render(request, "appone/StronaGlowna.html")

def Uslugi(request):
    return render(request, "appone/Uslugi.html")

def GotoweRozwiazania(request):
    context = Product.objects.all()
    return render(request, "appone/GotoweRozwiazania.html", {'products': context})

def Blog(request):
    return render(request, "appone/Blog.html")

def ONas(request):
    return render(request, "appone/ONas.html")

def Kontakt(request):
    return render(request, "appone/Kontakt.html")
