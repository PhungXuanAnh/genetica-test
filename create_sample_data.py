# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from gene.models import Gene, GeneActivity
from gene.enums import GeneActivityType, GeneLocation, GeneStatus


for _ in range(0, 1):
    gene = Gene.objects.create(
        processing_status=GeneStatus.PENDING,
        location=GeneLocation.GENETICA
    )
    GeneActivity.objects.create(
        gene_sample=gene,
        type=GeneActivityType.PENDING_AT_GENETICA
    )
    print(gene)
    print(gene.id)
    print(gene.last_activity)