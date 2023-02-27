from django.db import models

# Create your models here.
class Deck(models.Model):
    deck = models.CharField(max_length=100)
    cards = models.CharField(max_length=100)