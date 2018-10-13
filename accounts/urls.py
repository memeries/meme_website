from django.urls import path, include
from . import views

urlpatterns = [
    path('register/<slug:secret_token>/', views.register, name='register'),
    path('', include('django.contrib.auth.urls'))
]