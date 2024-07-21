from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    articles = Article.objects.all().values()
    if request.GET.get('search') and request.GET.get('search') != '':
        articles = Article.objects.filter(title__contains=request.GET.get('search'))
    data = {'articles': articles}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


@login_required(login_url='login')
def post_article(request):
    if request.method == "POST":
        full_text = request.POST.get('full-text')
        title = request.POST.get('title')
        Article.objects.create(user=request.user, title=title, full_text=full_text, date=datetime.utcnow())
        return redirect('home')
    return render(request, 'main/post_article.html')


def article_details(request, pk):
    article = Article.objects.get(pk=pk)
    user = User.objects.get(pk=article.user_id)
    comments = Comment.objects.all().filter(article=article)
    if request.method == "POST":
        comment_text = request.POST.get('comment')
        Comment.objects.create(user=request.user, article=article, full_text=comment_text, date=datetime.utcnow())
    data = {'article': article, 'user': user, 'comments': comments}
    return render(request, 'main/article_details.html', data)
