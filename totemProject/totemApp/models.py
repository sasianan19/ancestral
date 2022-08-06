from django.db import models

# Create your models here.
class Continents(models.Model):
    continent = models.CharField(max_length=50)

class Countries(models.Model):
    country = models.CharField(max_length=100)
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE)

class AnimalClass(models.Model):
    classification = models.CharField(max_length=100)

class Vertebrates(models.Model):
    classification = models.ForeignKey(AnimalClass, on_delete=models.CASCADE)
    animal = models.CharField(max_length=70)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    meaning = models.TextField(max_length=1000) 

class Invertebrates(models.Model):
    classification = models.ForeignKey(AnimalClass, on_delete=models.CASCADE)
    animal = models.CharField(max_length=70)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    meaning = models.TextField(max_length=1000) 