from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def home(request):
    articles = Article.objects.all()
    return render(request, 'news/home.html', {'articles': articles})


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, 'news/add_article.html', {'form': form})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            messages.success(request, 'Registration successful. You are now logged in.')

            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'news/article_detail.html', {'article': article})
