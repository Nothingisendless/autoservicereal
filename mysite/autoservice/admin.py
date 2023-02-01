from django.contrib import admin
from .models import (Automobilis,
                    AutomobilioModelis,
                    Paslauga,
                    Uzsakymas,
                    UzsakymoEilute,
                     Komentaras,
                     Profilis)
class UzsakymoEiluteInline(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0


class UzsakymoEiluteAdmin(admin.ModelAdmin):
    list_display = ('uzsakymas', 'paslauga', 'kiekis', 'kaina')

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis', 'data','terminas', 'vartotojas', 'suma')
    inlines = [UzsakymoEiluteInline]

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_modelis', 'valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis')
    search_fields = ('valstybinis_nr', 'vin-kodas')

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')

admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(AutomobilioModelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute, UzsakymoEiluteAdmin)
admin.site.register(Komentaras)
admin.site.register(Profilis)
