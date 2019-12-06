from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.index_list, name='index_list'),
    path('index_list', views.index_list, name='index_list'),
    path('index/contacto_list/', views.contacto_list, name='contacto_list'),
    path('index/galeria_list', views.galeria_list, name='galeria_list'),
    path('index/planes_list', views.planes_list, name='planes_list'),
]