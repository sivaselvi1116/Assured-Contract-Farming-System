from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def _str_(self):
        return self.name