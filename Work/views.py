from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Experiences

from datetime import datetime

current_year = datetime.now().year

# Create your views here.

def WorkPage(request):

    experiences_list = Experiences.objects.all().order_by('-entry_num')
    paginator = Paginator(experiences_list, 5)
    page_number = request.GET.get('page')
    experiences = paginator.get_page(page_number)

    return render(request, 'Work/Work_page.html', {'experiences':experiences, 'current_year':current_year})


def SingleWorkPage(request,pk):
    single_work = get_object_or_404(Experiences, id=pk)
    techs = single_work.techs_used
    techs = techs.replace(',',' ')
    tech_list = techs.split()
    #print(tech_list)


    return render(request,'Work/singleWork_page.html',{'single_work':single_work, 'tech_list':tech_list})