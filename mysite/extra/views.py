from django.shortcuts import render


def index(request):
    return render(request, 'extra/one.html')


def popup_css(request):
    return render(request, 'extra/popup.css')

def popup_js(request):
    return render(request, 'extra/popup.js')