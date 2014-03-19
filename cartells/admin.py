from django.contrib import admin
from cartells.models import *

# Register your models here.

class EnviamentAdmin(admin.ModelAdmin):
    list_display = ("nom","telefon","email","titol","arxiu")
    search_fields = ("email",)

# els elements concrets mostraran nomes el codi d'arxiu
admin.site.register(Cartell,EnviamentAdmin)
admin.site.register(Narracio,EnviamentAdmin)
admin.site.register(Poesia,EnviamentAdmin)
admin.site.register(Assaig,EnviamentAdmin)
# enviament (super-classe) mostrara dades del remitent
admin.site.register(Enviament,EnviamentAdmin)
