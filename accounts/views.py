from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import re


# Create your views here.

def contact(request):
    if request.method == 'POST' and 'btnsend' in request.POST:

        #var for fields
        name = None
        email = None
        phone = None
        message = None

        #get val from form
        if 'name' in request.POST: name = request.POST['name']
        else: messages.error(request, 'Error in name')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'Error in email')
        
        if 'phone' in request.POST: phone = request.POST['phone']
        else: messages.error(request, 'Error in phone')
        
        if 'message' in request.POST: message = request.POST['message']
        else: messages.error(request, 'Error in message')

        #check values
        if name and phone and email and message:
            contactprofile = ContactProfile(name=name, email=email, phone=phone, message=message)
            contactprofile.save()
            #success message
            messages.success(request, 'Message Send Success')
        else:
            messages.error(request,'Check empty fields')

        return redirect('contact')
    else:
        return render( request , 'accounts/contact.html')