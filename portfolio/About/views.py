from django.shortcuts import render

# Create your views here.

def AboutPage(request):
    return render(request, 'About/About_page.html', {})
