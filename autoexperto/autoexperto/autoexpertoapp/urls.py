from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name ='inicio'),
   path('nosotros', views.nosotros, name ='nosotros'),
    path('autos', views.autos, name ='autos'),
    path('crear', views.crear, name ='crear'),
    path('editar', views.editar, name ='editar'),
    path('form', views.autos, name ='form'),
    
    
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)