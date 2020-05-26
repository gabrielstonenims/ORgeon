from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')
    cover_pic = models.ImageField(blank=True, default='coverdefault.jpg', upload_to='cover_photos')
    fullname = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True,default='An employee of Orgeon of stars')
    bio = models.CharField(max_length=200, default='Just a music lover', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = output_size
            img.save(self.profile_pic.path)


class MyProfileUser(models.Model):
    profiler_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profiler_email