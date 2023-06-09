from django.contrib import admin

from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ['pk', 'debt_sum', 'notes_short']
    list_display_links = ['pk']


# admin.site.register(Debt, DebtAdmin)
# Register your models here.
