from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from contacts.models import Contact


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # for sending error if user already making inquiry.
        if request.user.is_authenticated:
            user_id = request.user.id

            has_connected = Contact.objects.all().filter(car_id=car_id, user_id=user_id)

            # if user_id is already exists
            if has_connected:
                messages.error(request, 'You already make inquiry please wait until get first response')
                return redirect('/cars/' + car_id)
        # save elements in contact model
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                          last_name=last_name, customer_need=customer_need, city=city
                          , state=state, email=email, phone=phone, message=message)
        # sending messages to admin whenever new inquiry posted .
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New inquiry',  # subject
            'You have new inquiry for ' + car_title + '. Please login to your admin panel',  # message
            'noreply1622@gmail.com',  # admin gmail
            [admin_email],
            fail_silently=False,
        )
        # saving post to models
        contact.save()
        # inquiry posted successfully to admin by customer
        messages.success(request, "Your inquiry saved we will back you soon")
        # redirect to cars page
        return redirect('/cars/' + car_id)
