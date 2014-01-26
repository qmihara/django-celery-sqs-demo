from django.db import models

class Item(models.Model):
    uuid = models.CharField(max_length=200)
    created_at = models.DateTimeField('created at')
