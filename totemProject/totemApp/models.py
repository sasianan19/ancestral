from django.db import models

# Create your models here.

class Continents(models.Model):
    # "unique = True" ensures that same value cannot be entered again if it is already present in database 
    continent = models.CharField(max_length = 50, unique = True)

    # "def __str__(self):" is a Python method that returns object in model class as a string
    # Will display the continent name rather than "Continents object (id)"
    def __str__(self):
        return self.continent

class AnimalClass(models.Model):
    classification = models.CharField(max_length = 100, unique = True)

    # Will display the classification name rather than "AnimalClass object (id)"
    def __str__(self):
        return self.classification

class Countries(models.Model):
    country = models.CharField(max_length = 100, unique = True)
    # "models.ForeignKey(Continents, ...)" accesses the list of continents in the Continents model so a specific continent
    # can be assigned to a country via a foreign key (the id of the assigned continent)
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE)

    # Will display the country name rather than "Countries object (id)"
    def __str__(self):
        return self.country

class Vertebrates(models.Model):
    # "models.ForeignKey(AnimalClass, ...)" and "models.ForeignKey(Countries, ...)" accesses the list of animal classes & countries in the 
    # AnimalClass & Countries models so specific classifications and countries can be assigned to a vertebrate or invertebrate via a foreign key 
    # (the id of the assigned classification or country)
    classification = models.ForeignKey(AnimalClass, on_delete = models.CASCADE)
    animal = models.CharField(max_length = 70)
    country = models.ForeignKey(Countries, on_delete = models.CASCADE)
    meaning = models.TextField(max_length = 5000) 

class Invertebrates(models.Model):
    classification = models.ForeignKey(AnimalClass, on_delete = models.CASCADE)
    animal = models.CharField(max_length = 70)
    country = models.ForeignKey(Countries, on_delete = models.CASCADE)
    meaning = models.TextField(max_length = 5000) 