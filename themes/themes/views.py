# themes/views.py
from django.shortcuts import render
from django.conf import settings
import os

def theme_list(request):
    # File path to lessons.txt
    file_path = os.path.join(settings.BASE_DIR, 'lessons.txt')
    with open(file_path, 'r') as file:
        themes = file.readlines()
    return render(request, 'themes/theme_list.html', {'themes': themes})
