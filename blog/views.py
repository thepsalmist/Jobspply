from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    latest_posts = Post.objects.order_by("-publish")[:4]
    paginator = Paginator(posts, 6)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "latest_posts": latest_posts,
        "page": page,
    }
    return render(request, "blog/post.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, slug=post, publish__year=year, publish__month=month, publish__day=day,
    )
    post_tags_id = post.tags.values_list("id", flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )
    context = {
        "post": post,
        "similar_posts": similar_posts,
    }
    return render(request, "blog/post-detail.html", context)


def search(request):
    queryset = Post.objects.all()
    latest_posts = Post.objects.order_by("-publish")[:4]
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(body__icontains=query)
        ).distinct()
    context = {
        "queryset": queryset,
        "latest_posts": latest_posts,
    }
    return render(request, "blog/search.html", context)
