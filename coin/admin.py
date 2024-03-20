from django.contrib import admin
from coin.models import Mining


class MiningAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity_mined",  )


admin.site.register(Mining, MiningAdmin)
