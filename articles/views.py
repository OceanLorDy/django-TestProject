from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles = Article.objects.all().order_by('name')
    return render(request, "articles/article_list.html", {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('article_list')
            except:
                pass
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})
