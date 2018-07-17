from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    msg = 'Welcome!'
    all_posts = Post.objects.all()
    return render(request, 'home/index.html', {'message': msg, 'posts': all_posts})
        # context안에 있는 Post 정보를 index.html로 전달
