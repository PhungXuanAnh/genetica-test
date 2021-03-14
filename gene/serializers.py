from rest_framework import serializers
from gene.models import Gene, GeneActivity
from gene.enums import *


class GeneSerializer(serializers.ModelSerializer):
    # activities = GeneActivitySerializer(read_only=True, many=True)

    class Meta:
        model = Gene
        fields = ['id', 'processing_status', 'location']


class GeneActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneActivity
        fields = ['id', 'gene_sample_id', 'type', 'attempts']
