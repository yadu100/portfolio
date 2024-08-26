from django.shortcuts import render
from .models import Projects

from datetime import datetime

current_year = datetime.now().year

# Create your views here.
def ProjectPage(request):

    projects = Projects.objects.all().order_by('-entry_num')

    return render(request,'Project/Project_page.html',{'projects':projects, 'current_year':current_year})


def SingleProjectPage(request,pk):
    project = Projects.objects.get(id = pk)
    techs = project.techs_used
    techs = techs.replace(',',' ')
    tech_list = techs.split()
    return render(request, 'Project/singleproject_page.html', {'project':project,'tech_list':tech_list})