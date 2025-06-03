from django.urls import path
from .views import PostUpdateView, PostDeleteView

urlpatterns = [
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]