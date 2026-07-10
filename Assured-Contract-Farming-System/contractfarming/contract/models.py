from django.db import models
from farmer.models import Farmer
from buyer.models import Buyer

class Contract(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    delivery_date = models.DateField()

    def _str_(self):
        return self.crop_name