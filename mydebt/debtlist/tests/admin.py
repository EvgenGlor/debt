from django.contrib import admin
from django.contrib.admin import ModelAdmin

from debtlist.models import Debt


@admin.register(Debt)
class DebtAdmin(ModelAdmin):
    pass
