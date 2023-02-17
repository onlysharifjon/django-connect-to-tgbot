from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title
