from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import FarmerForm


def farmer_register(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)

        if form.is_valid():
            form.save()

            # Go to Registration Successful page
            return redirect('success')

    else:
        form = FarmerForm()

    return render(request, 'farmer.html', {'form': form})