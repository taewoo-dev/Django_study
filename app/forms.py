from django import forms
from app.models import Post


# html 랜더링과 자원의 유효성 검사 역할 -> 유효성 검사는 models에서


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
