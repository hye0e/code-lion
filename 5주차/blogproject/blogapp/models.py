from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # 지금 생성하는 날짜를 저장하겠다는 의미
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title