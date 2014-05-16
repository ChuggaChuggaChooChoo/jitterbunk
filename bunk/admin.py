from django.contrib import admin
from bunk.models import Bunk


class BunkAdmin(admin.ModelAdmin):
    list_display = ['bunkFrom', 'bunkTo']

admin.site.register(Bunk, BunkAdmin)
