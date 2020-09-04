from django.db import models


# Create your models here.
class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_img = models.TextField()
    movie_createdate = models.CharField(max_length=100)
    movie_releasedate = models.CharField(max_length=100)
    movie_descrip = models.TextField()
