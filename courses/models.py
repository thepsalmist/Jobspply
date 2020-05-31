from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
