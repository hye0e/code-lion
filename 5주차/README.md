```
$ source myvenv/bin/activate
$ pip3 install django
$ python manage.py runserver
```
## 초기화
```
$ python manage.py migrate
```
## 데이터베이스 변경 사항이 생긴다면
```
$ python manage.py makemigrations
$ python manage.py migrate
```
---
## model.py에 테이블 설정
```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # 지금 생성하는 날짜를 저장하겠다는 의미
    date = models.DateTimeField(auto_now_add=True)

    # blogObject 대신 title을 이쁘게 나오게 하기위해
    def __str__(self):
        return self.title
```
```
$ python manage.py makemigrations
$ python manage.py migrate
```
## admin 사이트에서 보기 위해 admin.py 에 추가
```python
from .models import Blog
admin.site.register(Blog)
```
## admin 사이트에서 보기 위해 관리자계정 추가
```
$ python manage.py createsuperuser
```

## Django에서 사용자 입력을 받는 방법
> 1. HTML Form 이용하기
2. Django Form 이용하기
3. Django modelForm 이용하기

## HTML Form 이용하기
> 1. url 등록하기 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
]
```
> 2. view.py 에 함수 추가
```python
from django.shortcuts import render
from .models import Blog
from django.utils import timezone

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# create 는 실제로 글이 만들어지는 함수
def create(request):
    if(request.method == 'POST'):
        # 객체 생성
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # 저장
        post.save()
    return redirect('home')
```
> 3. html 추가
>> new.html 추가
```html
<form action="{% url 'create' %}" method="POST">
    {% csrf_token %}
    <div>
        <label for="title">제목</label><br/>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label for="body">본문</label><br/>
        <textarea name="body" id="body" cols="30" rows="10"></textarea>
    </div>
    <input type="submit" value="글 생성하기">
</form>
```
>> index.html 추가
<a href = "{% url 'new' %}">새 글 작성</a>

## Django Form 이용하기
> 1. url 등록하기 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),

    # Django form을 이용해 블로그 객체 만들기
    # Django는 하나의 url에서 GET, POST 둘다 요청 가능
    path('formcreate/'. views.formcreate, name = 'formcreate')
]
```
> 2. 어플리케이션안에 forms.py 추가
```python
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

```

> 3. view.py 에 함수 추가
```python
from .forms import BlogForm

# django form 을 이용해서 입력값을 받는 함수
# GET 요청 (= 입력 값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장하는 기능을 수행 즉, form에서 입력한 내용을 처리 )
# 둘 다 처리가 가능한 함수
def formcreate(request): 
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 저장해라
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else: 
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()
    # 세번째 인자는 딕셔너리 자료형으로 넘겨주어야함
    return render(request, 'form_create.html', {'form': form})

```
> 4. form_create.html 추가
```html
<h1>django form을 이용한 새 글 작성 페이지</h1> 
<form action="" method="POST">
    {% csrf_token %}
    <!-- 세번째 인자로 보냈던 form을 찍어줄 수 있음 -->
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="새 글 생성하기">
</form>
```