
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from pages.models import Team
from cars.models import Car


def home(requsest):
    # fetch all data from database to teams
    teams = Team.objects.all()
    # for showing featured car in the featured  car section
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields=Car.objects.values('model','city','year','body_style')

    # for finding distinct values of modal,city,year,body_style in search (home)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # pass dictionary of model team to pass data of teams model in html using data dictionary
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields':search_fields
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(requsest, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have new message from Carzone regarding ' + subject
        message_body = 'Name : ' + name + '. Email ' + email + '. Phone ' + phone + ' . Message ' + message
        # sending messages to admin whenever new inquiry posted .
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,  # subject
            message_body,  # message
            'noreply1622@gmail.com',  # admin gmail
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting .We will get you back shortly')
        return redirect('contact')
    return render(request, 'pages/contact.html')
