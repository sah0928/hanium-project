from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    content = models.TextField(null=True)             # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장
    # DB에서는 길이제한 유무에 따라서 문자열 필드타입이 다른다.
    # 길이 제한이 없는 문자열을 많이 쓰면 성능이 좋지 않다.

    def __str__(self):
        return self.title


class Test(models.Model):
    idtime = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    object = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    position_x = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    position_y = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    width = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    height = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    color_upper = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    color_lower = models.CharField(max_length=100) # 길이 제한이 있는 문자열

    def __str__(self):
        return self.idtime
