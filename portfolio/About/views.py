from django.shortcuts import render,redirect
from .models import Certifications

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages

import os

# Create your views here.

def AboutPage(request):

    certificates = Certifications.objects.all()
    return render(request, 'About/About_page.html', {'certificates':certificates})

def ContactPage(request):

    if request.method == 'POST':
        name = request.POST['Name']
        email_from = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']
        content = f"""
Message From
{name}

Message Content 
{message}

Reply mail        : {email_from}
                    
"""

        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_TO_USER],
            fail_silently=False

        )
        messages.success(request, "You mail was sent successfully")
        
        return redirect('contact')


    return render(request, 'About/contact.html',{})
