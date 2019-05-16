from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def index(request):
    category = Category.objects.all()
    post = Post.objects.all()
    return render(request, 'home/index.html', {"post": post,"category":category})

def detail(request, post_id):
    category = Category.objects.all()
    post = Post.objects.all()
    post_detail = Post.objects.get(pk=post_id)
    return render(request, 'home/detail.html', {"post_detail": post_detail, "post": post,"category":category})

def category(request, category_id):
    ctgr = Category.objects.all()
    post = Post.objects.filter(CategoryId=category_id)
    category = Category.objects.get(pk=category_id)
    allpost = Post.objects.all()
    return render(request, 'home/category.html', {"post": post,"category":category,"allpost":allpost,"ctgr":ctgr})

