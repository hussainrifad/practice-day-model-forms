from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name