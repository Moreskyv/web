from django.contrib import admin
from .models import Groups, Student, Teacher, Subject, Grade, Attendance

admin.site.register(Groups)
admin.site.register(Student)
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)