from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.
def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

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

# django form 을 이용해서 입력값을 받는 함수
# GET 요청 (= 입력 값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장하는 기능을 수행 즉, form에서 입력한 내용을 처리 )
# 둘 다 처리가 가능한 함수
def formcreate(request): 
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 저장로직
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

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm()
    # 세번째 인자는 딕셔너리 자료형으로 넘겨주어야함
    return render(request, 'form_create.html', {'form': form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    # pk 값이 blog_id인 Blog 객체를 가져와라
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄어주는 코드
    return render(request, 'detail.html', {'blog_detail': blog_detail})
