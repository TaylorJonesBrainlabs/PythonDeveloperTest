from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='countries-home'),
    path('about/', views.about, name='countries-about')
]
