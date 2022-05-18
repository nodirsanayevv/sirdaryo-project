from django.shortcuts import render
from blog.models import Course, Period

# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'base.html', {'courses':courses})




