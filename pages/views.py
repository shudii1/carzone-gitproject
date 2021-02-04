from django.shortcuts import render

# Create your views here.
from pages.models import Team


def home(requsest):
    # fetch all data from database to teams
    teams = Team.objects.all()
    # pass dictionary of model team to pass data of teams model in html using data dictionary
    data = {
        'teams': teams,
    }
    return render(requsest, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
