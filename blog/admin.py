from django.contrib import admin
from .models import Post
from .models import Item
from django import forms
from .models import Image

admin.site.register(Post)
admin.site.register(Item)

class ImageForm(forms.ModelForm):

   class Meta:
      model = Image
      fields = ['title','image']