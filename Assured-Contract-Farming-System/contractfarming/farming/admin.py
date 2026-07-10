from django.contrib import admin
from .models import Farmer, Crop, Buyer, Contract

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(Buyer)
admin.site.register(Contract)