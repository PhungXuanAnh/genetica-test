from django.contrib import admin
from gene.models import Gene, GeneActivity

class GeneAdmin(admin.ModelAdmin):
    fields = ['location', 'processing_status']
    list_display = ("id", "location", "processing_status")

admin.site.register(Gene, GeneAdmin)
