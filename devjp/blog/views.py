from django.shortcuts import render
from .models import Post, UploadVideos
# Create your views here.

def disply_data(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request,'image.html', context)

def video_display(request):
    songs = UploadVideos.objects.all()
    context = {
        'songs':songs
    }
    return render(request, 'video.html',context)
