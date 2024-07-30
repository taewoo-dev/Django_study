from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
