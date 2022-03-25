from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()) #Existe la fecha de publicación
    stuff_for_frontend={'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404 (Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        print(request.POST)
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html',stuff_for_frontend )

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':

            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                """ post.author = request.user """
                post.publised_date= timezone.now()
                post.save()
                return redirect('post_detail',pk=post.pk)
        else:
            form = PostForm(instance=post)
            stuff_for_frontend = {'form': form}
        return render (request, 'blog/post_edit.html', {'form': form})
