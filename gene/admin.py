import logging
from django.contrib import admin
from gene.models import Gene, GeneActivity

logger = logging.getLogger('app')

class GeneActivityAdmin(admin.ModelAdmin):
    fields = ['gene_sample', 'type', "created_by", "attempts"]
    list_display = ("gene_sample", "type", "created_by", "attempts")

class GeneActivityInline(admin.StackedInline):
    model = GeneActivity
    extra = 0

class GeneAdmin(admin.ModelAdmin):
    fields = ["owner", 'location', 'processing_status']
    list_display = ("owner", "location", "processing_status")
    inlines = [GeneActivityInline]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Gene, GeneAdmin)
admin.site.register(GeneActivity, GeneActivityAdmin)
