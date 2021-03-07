from django.urls import path
from .views import disply_data, video_display

urlpatterns = [
    path('', disply_data ),
    path('video/', video_display),
]