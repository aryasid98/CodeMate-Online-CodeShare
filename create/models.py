from django.db import models

# Create your models here.
class create_code(models.Model):
    slug=models.CharField(max_length=10)
    lang=models.CharField(max_length=100)
    content=models.CharField(max_length=10000)
    expire=models.CharField(max_length=100)

    def __str__(self):
        return self.content
