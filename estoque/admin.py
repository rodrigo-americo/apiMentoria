from django.contrib import admin
from .models import Pc


class PcAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'classroom', 'ssd', 'createdAt', 'updatedAt',)
    search_fields = ('is', 'model', 'ssd',)
    list_filter = ('ssd',)


admin.site.register(Pc, PcAdmin)
