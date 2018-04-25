from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The index page (home page)
    path('contact/', views.contact, name='contact')
]
