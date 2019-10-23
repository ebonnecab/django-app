from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name

class Toppings(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name