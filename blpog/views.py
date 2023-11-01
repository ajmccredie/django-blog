from django.shortcuts import render
from django.view import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.obhects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
