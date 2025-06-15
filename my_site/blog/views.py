from django.shortcuts import render
from datetime import date
all_posts = [
    {"slug": "hike-in-the-mountains",
     "image": "mountains.jpg",
     "author": "Maximilian",
     "date": date(2021, 7, 21),
     "title": "Mountain Hiking",
     "excerpt": "There's nothing like the views you get when hiking in the mountains",
     "content": """lorem ipsum"""},
    {"slug": "hiking-in-the-woods",
     "image": "woods.jpg",
     "author": "Maximilian",
     "date": date(2025, 6, 15),
     "title": "Woods Hiking",
     "excerpt": "There's nothing like the views you get when hiking in the mountains",
     "content": """lorem ipsum"""},
    {"slug": "windsurfing",
     "image": "mountains.jpg",
     "author": "Maximilian",
     "date": date(2024, 7, 12),
     "title": "Windsurfing",
     "excerpt": "There's nothing like the views you get when hiking in the mountains",
     "content": """lorem ipsum"""},
    {"slug": "mushrooms",
     "image": "mountains.jpg",
     "author": "Maximilian",
     "date": date(2023, 8, 5),
     "title": "Mushrooms",
     "excerpt": "There's nothing like the views you get when hiking in the mountains",
     "content": """lorem ipsum"""},
    {"slug": "skiing",
     "image": "mountains.jpg",
     "author": "Maximilian",
     "date": date(2023, 8, 5),
     "title": "Skiing in Italy",
     "excerpt": "There's nothing like the views you get when hiking in the mountains",
     "content": """lorem ipsum"""}
]
# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):

    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    return render(request, "blog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    sorted_posts = sorted(all_posts,key=get_date)

    return render(request, "blog/all-posts.html",{
        "all_posts": sorted_posts
    })

def post_detail(request, slug):
    post =  next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post": post,
    })
