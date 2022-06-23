## 가상환경 생성
```
$ python3 -m venv myvenv
```
## django 설치
```
$ pip3 install django
```
## 프로젝트 생성
```
$ django-admin startproject static_ex
```
## 어플리케이션 생성
```
$ cd static_ex
$ python manage.py startapp staticapp
```
## settings 추가
```
INSTALLED_APPS 에 staticapp 추가
```
## views 설정
```python
def home(request):
    return render(request, 'home.html')
```
## template 추가
```
$ mkdir templates
home.html 추가
```
## 최상위 프로젝트에 static 추가
```
$ mkdir static
```

```python
# setting.py 에 설정 추가
# 최상위 폴더 -> BASE_DIR
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# 어플리케이션에서만 사용하는 Static File이 있을 경우
# 어플리케이션 안에 static 폴더 만들기
import os
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'staticapp', 'static')
]
```
## home.html 에 추가
```html
{% load static %}

# head태그 안에 추가
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
```

## 배포 시엔 static files 를 한 폴더안에 정리한다.
```python
# setting.py
STATIC_ROOT = os.path.join('staticfiles')
```

## static 파일들이 staticfiles 안에 모아지는 명령어
```
$ python manage.py collectstatic
```