from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect('/success/')
