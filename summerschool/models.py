from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import  timezone


SCHOOL_LEVELS = (
    ("GradeSchool", "GradeSchool"),
    ("PreSchool", "PreSchool"),
    ("Kindergarten", "Kindergarten")
)

GRADE_LEVEL = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ('7', '7'),
    ("8", "8"),
)


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    school = models.CharField(max_length=20, choices=SCHOOL_LEVELS)
    fullname = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(default=10, blank=True)
    grade = models.CharField(max_length=3, choices=GRADE_LEVEL,blank=True,help_text="Please leave this field blank when your school is not GradeSchool,thank you")
    photo = models.ImageField(upload_to="kids_grade_school_photos", blank=True, default="kid.jpg")
    name_of_parent_or_guardian = models.CharField(max_length=150, blank=True)
    contact_number = models.CharField(max_length=30, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = output_size
            img.save(self.photo.path)


class Student(models.Model):
    student_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_email


class SchoolLoginCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.date_logged}"