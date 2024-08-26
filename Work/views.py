from django.shortcuts import render
from .models import Experiences

from datetime import datetime

current_year = datetime.now().year

# Create your views here.

def WorkPage(request):

    experiences = Experiences.objects.all().order_by('-entry_num')

    return render(request, 'Work/Work_page.html', {'experiences':experiences, 'current_year':current_year})


def SingleWorkPage(request,pk):
    single_work = Experiences.objects.get(id=pk)
    techs = single_work.techs_used
    techs = techs.replace(',',' ')
    tech_list = techs.split()
    #print(tech_list)


    return render(request,'Work/singleWork_page.html',{'single_work':single_work, 'tech_list':tech_list})