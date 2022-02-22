from django.db import models

class Weerdata(models.Model):
    temperatuur = models.FloatField()
    luchtdruk = models.FloatField()
    luchtvochtigheid = models.FloatField()
