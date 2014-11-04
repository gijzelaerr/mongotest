from django.contrib import admin
from .models import Something


class SomethingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Something, SomethingAdmin)