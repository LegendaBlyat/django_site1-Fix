from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, max_length=255)
    video = models.FileField(upload_to="blog/%y")


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length= 255, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)


    def repr(self):
        return 'Image(%s, %s)' % (self.title, self.image)

    def str (self):
        return self.title

class Item(models.Model):
    name= models.CharField(max_length=200)
    body= models.TextField(max_length=500)

    date= models.DateTimeField(default=timezone.now)