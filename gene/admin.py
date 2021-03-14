from django.contrib import admin
from gene.models import Gene, GeneActivity


class GeneActivityAdmin(admin.ModelAdmin):
    fields = ['gene_sample', 'type', "created_by", "attempts"]
    list_display = ("gene_sample", "type", "created_by", "attempts")

class GeneActivityInline(admin.StackedInline):
    model = GeneActivity
    extra = 0

class GeneAdmin(admin.ModelAdmin):
    fields = ['location', 'processing_status']
    list_display = ("id", "location", "processing_status")
    inlines = [GeneActivityInline]


admin.site.register(Gene, GeneAdmin)
admin.site.register(GeneActivity, GeneActivityAdmin)
