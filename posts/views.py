from django.views.generic import (
    listView,
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



