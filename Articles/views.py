from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Articles
from datetime import datetime

current_year = datetime.now().year

from .utils import SearchItem
# Create your views here.

def ArticlesPage(request):

    articles,search_query = SearchItem(request)
    no_of_items = articles.count()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    articles_page = paginator.get_page(page_number)

    return render(request, 'Articles/Articles_page.html',{'articles':articles_page, 'search_query':search_query, 'no_of_items':no_of_items, 'current_year':current_year})


def SingleArticlePage(request,pk):
    single_article = get_object_or_404(Articles, id=pk)
    return render(request, 'Articles/singleArticle_page.html',{'single_article':single_article})