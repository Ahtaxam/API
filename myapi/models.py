from django.db import models
import datetime

# Create your models here.


class TODO(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(datetime.date.today())

    def __str__(self):
        return self.title
