from django.shortcuts import render, get_list_or_404
# from django.http import HttpResponse 
from .models import News, Category
from .forms import NewForm

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def view_news(request,news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request,'news/view_news.html', {'news_item': news_item})

def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewForm()
    return render(request, 'news/add_news.html', {'form': form})


