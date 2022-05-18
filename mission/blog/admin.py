from django.contrib import admin
from .models import Course, Period, PracticeWorker, Certificate
# Register your models here.


admin.site.register(Course),
admin.site.register(Period),
admin.site.register(PracticeWorker)
admin.site.register(Certificate)