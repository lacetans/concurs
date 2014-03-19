from django.contrib import admin
from cartells.models import *

# Register your models here.

class EnviamentAdmin(admin.ModelAdmin):
    list_display = ("nom","telefon","email","titol","arxiu")
    search_fields = ("email",)

# els elements concrets mostraran nomes el codi d'arxiu
admin.site.register(Cartell)
admin.site.register(Narracio)
admin.site.register(Poesia)
admin.site.register(Assaig)
# enviament (super-classe) mostrara dades del remitent
admin.site.register(Enviament,EnviamentAdmin)
