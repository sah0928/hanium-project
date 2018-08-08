from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    msg = 'Welcome!'
    all_posts = Post.objects.all()
    form = PostForm()

    ### post 추가 코드 ###
    # new_post = Post(title="add title", content="추가")
    # new_post.save()

    return render(request, 'home/index.html', {'message': msg, 'posts': all_posts, 'form': form})
    # context안에 있는 Post 정보를 index.html로 전달


def search(request):
    all_posts = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        all_posts = all_posts.filter(title__icontains=q)
    return render(request, 'home/search.html', {'posts': all_posts, 'keyword': q})

    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         msg = "success"
    #         keyword = request.POST['title']
    #         all_posts = all_posts.get(title__icontains=keyword)
    #         return render(request, 'home/search.html', {'message': msg, 'keyword': keyword})
    # else:
    #     msg = "fail"
    #
    # return render(request, 'home/search.html', {'message': msg})
