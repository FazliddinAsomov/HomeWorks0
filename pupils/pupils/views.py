# pupils/views.py
from django.shortcuts import render
from .models import Pupil

def pupil_list(request):
    pupils = Pupil.objects.all()
    return render(request, 'pupils/pupil_list.html', {'pupils': pupils})
