from django.shortcuts import render,redirect
from .models import Certifications

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages

from datetime import datetime

current_year = datetime.now().year


# Create your views here.

def AboutPage(request):

    certificates = Certifications.objects.all()
    return render(request, 'About/About_page.html', {'certificates':certificates, 'current_year':current_year})

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

        try:
            send_mail(
                subject,
                content,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_TO_USER],
                fail_silently=False,
            )
            messages.success(request, "Your message was sent successfully.")
        except Exception:
            messages.error(request, "Failed to send your message. Please try again later.")
        
        return redirect('contact')


    return render(request, 'About/contact.html',{'current_year':current_year})
