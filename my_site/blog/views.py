from django.shortcuts import render
from datetime import date
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm

all_posts = Post.objects.all().order_by("-date")
recent_posts = all_posts[:3]
# Create your views here.
def get_date(post):
    return post['date']


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(request):
#     return render(request, "blog/index.html",{
#         "posts": recent_posts
#     })


class AllPosts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     return render(request, "blog/all-posts.html",{
#         "all_posts": all_posts
#      })

# def post_detail(request, slug):
#     post =  next(post for post in all_posts if post.slug == slug)
#     return render(request, "blog/post-detail.html",{
#         "post": post,
#     })

class PostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context