from django.urls import path
from . import views

urlpatterns = [
    path("", views.StrtingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPosts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail-page")
]