from django.db import models


class Farmer(models.Model):
    farmer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def _str_(self):
        return self.farmer_name


class Crop(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    expected_price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.crop_name


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def _str_(self):
        return self.buyer_name


class Contract(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    contract_date = models.DateField()

    def _str_(self):
        return f"{self.farmer.farmer_name} - {self.crop.crop_name}"
