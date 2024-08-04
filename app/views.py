from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from app.forms import PostForm
from app.models import Post


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    # qs = [
    #     {"id": 1, "title": "post #1"},
    #     {"id": 2, "title": "post #2"},
    # ]
    # render는 세번째 인자로 Queryset을 전달
    return render(
        request,
        "app/index.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    # resource가 없는 요청에 대한 응답은 404 error
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )


post_new = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    success_url="/app/",
)
