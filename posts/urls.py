from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/", views.PostDeleteView.as_view(), name="delete"),
]

