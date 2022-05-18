from gettext import NullTranslations
from tkinter import CASCADE
from turtle import title
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    

    def __str__(self):
        return self.name

class Period(models.Model):
    period = models.CharField(blank=True, null=True, max_length=255)


    def __str__(self):
        return self.period



class PracticeWorker(models.Model):
    f_name = models.CharField(max_length=255, blank=True, null=True)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    s_name = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    period_id = models.ForeignKey(Period, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Certificate(models.Model):
    practiceworker_id = models.ForeignKey(PracticeWorker, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='files')

    def __str__(self) -> str:
        return str(self.id)