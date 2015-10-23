from django.shortcuts import render
from .models import Post

# Create your views here.
# 
# def post_list(request):
#     post = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'post':post})

def post_list(request):
    #posts    =    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts    =    Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})