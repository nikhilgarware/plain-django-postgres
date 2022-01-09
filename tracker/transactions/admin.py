from django.contrib import admin
from transactions import models


# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date", "brief_description", "amount", "transaction_type")


admin.site.register(models.Transaction, TransactionAdmin)
