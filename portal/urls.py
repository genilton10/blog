from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
	#Areas
    path('area', views.area_list, name='area_list'),
    path('area/<int:pk>/', views.area_detail, name='area_detail'),
    path('area/new', views.area_new, name='area_new'),
    path('area/<int:pk>/edit/', views.area_edit, name='area_edit'),
   	path('area/<pk>/remove/', views.area_remove, name='area_remove'),
   	#Noticias
   	path('noticia', views.noticia_list, name='noticia_list'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),
    path('noticia/new', views.noticia_new, name='noticia_new'),
    path('noticia/<int:pk>/edit/', views.noticia_edit, name='noticia_edit'),
   	path('noticia/<pk>/remove/', views.noticia_remove, name='noticia_remove'),
]
