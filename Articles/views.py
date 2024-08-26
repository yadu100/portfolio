from django.shortcuts import render
from . models import Articles
from datetime import datetime

current_year = datetime.now().year

from .utils import SearchItem
# Create your views here.

def ArticlesPage(request):

    articles,search_query = SearchItem(request)
    no_of_items = len(articles)

    return render(request, 'Articles/Articles_page.html',{'articles':articles, 'search_query':search_query, 'no_of_items':no_of_items, 'current_year':current_year})


def SingleArticlePage(request,pk):
    single_article = Articles.objects.get(id=pk)
    return render(request, 'Articles/singleArticle_page.html',{'single_article':single_article})