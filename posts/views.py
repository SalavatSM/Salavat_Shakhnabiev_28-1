from datetime import date

from django.shortcuts import HttpResponse, redirect, render

from posts.models import Post
from posts.models import Product

# Create your views here.
""" MVC - Model View Controller """

""" Controller's """


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)

