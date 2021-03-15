from gene.enums import GeneLocation, GeneStatus, GeneActivityType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Gene(models.Model):
    owner = models.CharField(max_length=100, null=True, blank=True)
    processing_status = models.IntegerField(choices=GeneStatus.choices())
    location = models.IntegerField(choices=GeneLocation.choices())
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        default=timezone.now,
        editable=False,
        help_text=_("Created at."),
    )
    
    @property
    def last_activity(self):
        return GeneActivity.objects.filter(gene_sample=self).order_by('created_at').first()

class GeneActivity(models.Model):
    gene_sample = models.ForeignKey(Gene, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        default=timezone.now,
        editable=False,
        help_text=_("Created at."),
    )
    type = models.IntegerField(choices=GeneActivityType.choices())
    note = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.CharField(default="Created by someone", max_length=100)
    attempts = models.IntegerField(default=1)
