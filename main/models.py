from __future__ import unicode_literals

from django.db import models


# Create your models here.

class MainModel(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name
