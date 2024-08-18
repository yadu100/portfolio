from django.shortcuts import render
from .models import Experiences

# Create your views here.

def WorkPage(request):

    experiences = Experiences.objects.all()

    return render(request, 'Work/Work_page.html', {'experiences':experiences})

