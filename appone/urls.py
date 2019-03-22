from django.urls import path, re_path
from appone import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appone'

urlpatterns = [
    path('uslugi/', views.Uslugi,name='Uslugi'),
    path('gotowerozwiazania/', views.GotoweRozwiazania, name='GotoweRozwiazania'),
    path('blog/', views.Blog, name='Blog'),
    path('onas/', views.ONas, name='ONas'),
    path('kontakt/', views.Kontakt, name='Kontakt')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
