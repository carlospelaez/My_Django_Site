from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()) #Existe la fecha de publicación
    stuff_for_frontend={'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)