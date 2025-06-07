from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy

class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "author"
    ]

class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("list")

class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "author"
    ]
    success_url = reverse_lazy("list") 


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post

    
 





