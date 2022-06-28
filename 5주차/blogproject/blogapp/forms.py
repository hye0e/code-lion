from django import forms
from .models import Blog
class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # 입력 값
        # 아래와 같이 입력 하게 된다면 Blog Model에 있는 모든 값들을 field로 받겠다라는 의미
        # fields = '__all__'
        # 특정 필드만 입력받고 싶다면,
        fields = ['title', 'body']