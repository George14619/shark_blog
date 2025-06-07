from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
]

