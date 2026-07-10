from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.conf import settings

from farmer.models import Farmer
from buyer.models import Buyer
from .models import Contract


def home(request):
    return render(request, "index.html")


def dashboard(request):
    context = {
        "farmer_count": Farmer.objects.count(),
        "buyer_count": Buyer.objects.count(),
        "contract_count": Contract.objects.count(),
    }
    return render(request, "dashboard.html", context)


def create_contract(request):
    if request.method == "POST":

        farmer = Farmer.objects.get(id=request.POST["farmer"])
        buyer = Buyer.objects.get(id=request.POST["buyer"])

        crop_name = request.POST["crop_name"]
        quantity = request.POST["quantity"]
        price = request.POST["price"]
        delivery_date = request.POST["delivery_date"]

        Contract.objects.create(
            farmer=farmer,
            buyer=buyer,
            crop_name=crop_name,
            quantity=quantity,
            price=price,
            delivery_date=delivery_date
        )

        send_mail(
            subject="Contract Created Successfully",
            message=f"""
Hello {buyer.name},

Your contract has been created successfully.

Farmer : {farmer.name}
Crop : {crop_name}
Quantity : {quantity}
Price : {price}
Delivery Date : {delivery_date}

Thank you for using the Assured Contract Farming System.
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["sivaselvil907@gmail.com"],
            fail_silently=False,
        )

        return redirect("/success/")

    return render(request, "create_contract.html")
