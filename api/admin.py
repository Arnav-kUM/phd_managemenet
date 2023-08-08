from django.contrib import admin
from .models import Student, Instructor, Advisor, Logbook

# Register your models here.
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Advisor)
admin.site.register(Logbook)