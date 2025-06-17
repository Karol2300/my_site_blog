from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = Post.objects.all().order_by("date")
recent_posts = all_posts[1:]
# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):
    return render(request, "blog/index.html",{
        "posts": recent_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
     })

def post_detail(request, slug):
    post =  next(post for post in all_posts if post.slug == slug)
    return render(request, "blog/post-detail.html",{
        "post": post,
    })
