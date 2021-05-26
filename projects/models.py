from django.db import models
from django.db.models.fields import CharField, EmailField, URLField

from mentors.models import Mentor

#model class for project
class Project(models.Model):
    title = models.CharField(max_length=80, default='')
    description = models.TextField(default='')
    code = models.CharField(max_length=8, default='')
    stack = models.CharField(max_length=100, default='')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

