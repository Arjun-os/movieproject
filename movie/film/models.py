from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    image = models.ImageField(upload_to="film/image",null=True,blank=True)

    def __str__(self):
        return self.title

