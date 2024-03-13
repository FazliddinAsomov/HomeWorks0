# pupils/models.py
from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=100)
    exam_scores = models.CharField(max_length=100)  # You might need a better field type for scores

    def __str__(self):
        return self.name
