from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.validators import FileExtensionValidator
from datetime import date,time,datetime,timedelta

PARTNERSHIP_TYPE = (
    ("personal","personal"),
    ('government','government'),
    ('corporate supply','corporate supply'),
    ('equipment and supply','equipment and supply')
)

FEELINGS_CHOICES = (
    ("Happy","Happy"),
    ("Sad","Sad"),
    ("Confued","Confued"),
    ("Smiling","Smiling"),
    ("Crying","Crying"),
    ("Winki","Winki"),
    ("Chilling","Chilling"),
)

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    why_join_Orgeon = models.CharField(max_length=200)
    # volunteering_as = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='volunteers_pics',default='default.jpg',validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    date_volunteered = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.name} has volunteered."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.photo.path)


class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    theme = models.CharField(max_length=100)
    venue = models.CharField(max_length=150)
    date_of_event = models.DateField(default=timezone.now)
    # event_started = models.BooleanField(default=False,)
    event_poster = models.ImageField(upload_to='event_pics',blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    description_of_event = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.theme}"

    def get_absolute_event_url(self):
        return reverse("event_detail",args={self.id })


class JoinTrip(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} has decided to join the trip."

class Partnership(models.Model):
    partnership = models.CharField(choices=PARTNERSHIP_TYPE,max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.partnership}"

class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"

class NewsUpdate(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Report(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    report = models.TextField()
    has_read = models.ManyToManyField(User,related_name="has_read_report",blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s report = {self.title}"

    def get_absolute_url(self):
        return reverse("report_detail",args={self.pk})


class InstantMessage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_user')
    recipient = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recipient',blank=True,null=True,help_text="Please select just one employee.")
    message_content = models.TextField()
    read = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender} has sent a private message to { self.recipient.username }."

    def get_absolute_instant_message_url(self):
        return reverse("inmessage_detail",args={ self.pk })


    def message_count(self):
        return self.message_content.count

class Usermsg(models.Model):
    unread_message = models.ForeignKey(InstantMessage,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.unread_message.title}"


class Post(models.Model):
    author = author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title = models.CharField(max_length=200)
    message = models.TextField(help_text="This message would be sent to all employees")
    poster = models.ImageField(upload_to="post_posters",blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])],help_text="Leave this field blank if message has no image.")
    views = models.IntegerField(default=0)
    has_read = models.ManyToManyField(User,related_name="has_read_post", blank=True)
    need_replies = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{ self.title }"

    def get_absolute_post_url(self):
        return reverse("post_detail",args={self.pk })


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.poster.path)

class Comments(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    reply = models.TextField()
    date_posted  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} has commented on {self.post }"



class Gallery(models.Model):
    image_caption = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to="galleries")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.image_caption} "