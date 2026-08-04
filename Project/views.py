from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Projects

from datetime import datetime

current_year = datetime.now().year

# Create your views here.
def ProjectPage(request):

    projects_list = Projects.objects.all().order_by('-entry_num')
    paginator = Paginator(projects_list, 5)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(request,'Project/Project_page.html',{'projects':projects, 'current_year':current_year})


def SingleProjectPage(request,pk):
    project = get_object_or_404(Projects, id=pk)
    techs = project.techs_used
    techs = techs.replace(',',' ')
    tech_list = techs.split()
    return render(request, 'Project/singleproject_page.html', {'project':project,'tech_list':tech_list})