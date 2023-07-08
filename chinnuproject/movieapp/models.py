from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    dep=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=250)
    course=models.TextField()
    def __str__(self):
        return self.name