from django.shortcuts import render


# Create your views here.

def home(requsest):
    return render(requsest, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
