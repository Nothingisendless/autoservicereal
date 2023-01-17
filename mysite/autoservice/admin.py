from django.contrib import admin
from .models import (Automobilis,
                    AutomobilioModelis,
                    Paslauga,
                    Uzsakymas,
                    UzsakymoEilute)


admin.site.register(Automobilis)
admin.site.register(AutomobilioModelis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(UzsakymoEilute)

