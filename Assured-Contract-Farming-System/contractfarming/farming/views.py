from django.shortcuts import render
from farmer.models import Farmer
from buyer.models import Buyer
from contract.models import Contract

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "index.html")

def dashboard(request):
    context = {
        "farmer_count": Farmer.objects.count(),
        "buyer_count": Buyer.objects.count(),
        "contract_count": Contract.objects.count(),
    }
    return render(request, "dashboard.html", context)
def success(request):
    return render(request,"success.html")