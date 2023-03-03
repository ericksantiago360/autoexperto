from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('nosotros', views.nosotros, name ='nosotros'),
    path('autos', views.autos, name ='autos'),
    path('contacto', views.contacto, name ='contacto'),
    path('autos/crear', views.crear, name = 'crear_auto'),
    path('editar', views.editar, name ='editar_autos'), 
    path('form', views.autos, name ='form'),
    
    
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)