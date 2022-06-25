from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class PostListView(ListView):
    model= Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy["blog:all"]

class PostDetailView(DetailView):
    model=Post

class PostUpdateView:
    model = Post
    fields = "__all__"
    success_url: reverse_lazy["blog:all"]

class PostDeleteView:
    model = Post
    fields = "__all__"
    success_url: reverse_lazy["blog:all"]
