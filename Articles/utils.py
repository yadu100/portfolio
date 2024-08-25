from .models import Articles
from django.db .models import Q

def SearchItem(request):
        search_query = ''
        articles = Articles.objects.all().order_by('-created')
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')

            articles = Articles.objects.distinct().filter(
                Q(heading__icontains=search_query) | 
                Q(key_point__icontains=search_query) |
                Q(primary_note__icontains=search_query) |
                Q(sub_heading1__icontains=search_query) |
                Q(sub_text1__icontains=search_query) |
                Q(sub_heading2__icontains=search_query) |
                Q(sub_text2__icontains=search_query) |
                Q(sub_heading3__icontains=search_query) |
                Q(sub_text3__icontains=search_query) |
                Q(sub_heading4__icontains=search_query) |
                Q(sub_text4__icontains=search_query) |
                Q(sub_heading5__icontains=search_query) |
                Q(sub_text5__icontains=search_query) |
                Q(conclusion__icontains=search_query)).order_by('-created')
        
        return articles, search_query
            