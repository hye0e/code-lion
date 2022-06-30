from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # setting에 설정된 파일 경로 안에 blog_photo 폴더를 생성하여 그곳에 저장하겠다라는 의미
    photo = models.ImageField(blank = True, null = True, upload_to = 'blog_photo')
    # 지금 생성하는 날짜를 저장하겠다는 의미
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title