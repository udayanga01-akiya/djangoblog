from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]