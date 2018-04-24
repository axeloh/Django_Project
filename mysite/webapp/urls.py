#from django.conf.urls import url
from django.urls import path
from . import views  # Import from current package

urlpatterns = [
    path('', views.index, name='index')
]