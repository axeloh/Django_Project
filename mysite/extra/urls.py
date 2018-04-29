from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popup.css', views.popup_css, name='popup_css'),
    path('popup.js', views.popup_js, name='popup_js')
]
