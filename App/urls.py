from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.inicio, name='inicio'),
    path('almacen', views.almacen, name="almacen"),
    path('produccion', views.produccion, name="produccion"),
    path('calidad', views.calidad, name="calidad"),
    path('reportes', views.reportes, name="reportes"),
    
]