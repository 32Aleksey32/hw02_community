from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LIMIT = 10


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT]
    # В словаре context отправляем информацию в шаблон
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


# Страница с постами
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[:LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
