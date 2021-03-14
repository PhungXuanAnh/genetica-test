# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from gene.models import Gene, GeneActivity
from gene.enums import GeneActivityType, GeneLocation, GeneStatus

names = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C"]
for name in names:
    gene = Gene.objects.create(
        owner=name,
        processing_status=GeneStatus.PENDING,
        location=GeneLocation.GENETICA
    )
    GeneActivity.objects.create(
        gene_sample=gene,
        type=GeneActivityType.PENDING_AT_GENETICA
    )
