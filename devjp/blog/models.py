from django.db import models


# Create your models here

class Post(models.Model):
    title = models.CharField(max_length=120)
    image_field = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class UploadVideos(models.Model):
    title = models.CharField(max_length=100)
    songs = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title


