from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Handles what the end-user "views" or interacts with

def index(request):
    return HttpResponse("<h2>HEY!</h2>")