from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')
    cover_pic = models.ImageField(blank=True, default='coverdefault.jpg', upload_to='cover_photos')
    fullname = models.CharField(max_length=150,blank=True)
    position = models.CharField(max_length=100,blank=True,default='An employee of Orgeon of stars')
    bio = models.CharField(max_length=200, default='Just a music lover', blank=True)
    


    def __str__(self):
        return f"{ self.user.username }'s profile"

  
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.profile_pic.path)

