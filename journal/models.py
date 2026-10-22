from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Subject(models.Model):
    title = models.CharField(max_length=150)
    teachers = models.ManyToManyField(Teacher, related_name='subjects')

    def __str__(self):
        return self.title

class Grade(models.Model):
    value = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')

    def __str__(self):
        return f'Оценка {self.value} для {self.student} по предмету {self.subject}'

class Attendance(models.Model):
    date = models.DateField()
    present = models.BooleanField(default=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')

    def __str__(self):
        status = "Присутствовал" if self.present else "Отсутствовал"
        return f'{self.student} - {self.subject} ({self.date}): {status}'