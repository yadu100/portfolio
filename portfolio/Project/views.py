from django.shortcuts import render
from .models import Projects

# Create your views here.
def ProjectPage(request):

    projects = Projects.objects.all().order_by('-entry_num')

    return render(request,'Project/Project_page.html',{'projects':projects})