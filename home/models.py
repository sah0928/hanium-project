from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신시 현재 시간 자동저장

    def __str__(self):
        return self.title


class Person(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # 이미지시간 + idx (201808301, 201808302 ...)
    label = models.CharField(max_length=100)  # 사람의 임시 id (person1, person2 ...)
    positionX = models.CharField(max_length=100)
    positionY = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    colorUpper = models.CharField(max_length=100)
    colorLower = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Photo(models.Model):
    time = models.DateTimeField(auto_now_add=True, primary_key=True)  # 해당 레코드 생성시 현재 시간 자동저장
    image = models.ImageField(upload_to="img")

    def __str__(self):
        return self.time

