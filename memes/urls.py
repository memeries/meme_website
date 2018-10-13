from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/<int:type_id>/', views.type, name='type'),
    path('un_safe/', views.un_safe, name='un_safe'),
]