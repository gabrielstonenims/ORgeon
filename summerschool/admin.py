from django.contrib import admin
from .models import School, Student, SchoolLoginCode

admin.site.register(School)
admin.site.register(Student)
admin.site.register(SchoolLoginCode)
