from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status

from gene.models import Gene, GeneActivity
from gene.serializers import GeneSerializer
from gene.enums import *


class GenelViewSet(viewsets.ModelViewSet):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["put"])
    def verify(self, request, *args, **kwargs):
        instance = self.get_object()
        if (
            instance.processing_status == GeneStatus.PENDING
            and instance.location == GeneLocation.HANOI_LAB
        ):
            instance.processing_status = GeneStatus.VERIFIED
            __ = GeneActivity.objects.create(
                type=GeneActivityType.VERIFY, gene_sample_id=instance.id, attempts=1
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data, status=status.HTTP_200_OK
            )
        return Response(
            data="Gene sample is not pending status or not in Hanoi Lab",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["put"])
    def extract(self, request, *args, **kwargs):
        instance = self.get_object()
        if (
            instance.processing_status == GeneStatus.PACKAGED
            and instance.location == GeneLocation.USA_LAB
        ):
            instance.processing_status = GeneStatus.EXTRACTED
            __ = GeneActivity.objects.create(
                type=GeneActivityType.EXTRACT, gene_sample_id=instance.id, attempts=1
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data, status=status.HTTP_200_OK
            )
        return Response(
            data="Gene sample is not package status or not in USA Lab",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["put"])
    def package(self, request, *args, **kwargs):
        instance = self.get_object()
        if (
            instance.processing_status == GeneStatus.PENDING
            and instance.location == GeneLocation.GENETICA
        ):
            instance.processing_status = GeneStatus.PACKAGED
            __ = GeneActivity.objects.create(
                type=GeneActivityType.PACKAGE, gene_sample_id=instance.id, attempts=1
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data, status=status.HTTP_200_OK
            )
        return Response(
            data="Gene sample is not pending status or not in Genetica",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["put"])
    def decode(self, request, *args, **kwargs):
        instance = self.get_object()
        if (
            instance.processing_status == GeneStatus.EXTRACTED
            and instance.location == GeneLocation.USA_LAB
        ):
            instance.processing_status = GeneStatus.DECODED
            __ = GeneActivity.objects.create(
                type=GeneActivityType.DECODE, gene_sample_id=instance.id, attempts=1
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data, status=status.HTTP_200_OK
            )
        return Response(
            data="Gene sample is not extracted status or not in USA Lab",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["put"])
    def send(self, request, *args, **kwargs):
        location = request.data["location"]
        instance = self.get_object()
        if (
            location == GeneLocation.HANOI_LAB
            and instance.location == GeneLocation.GENETICA
            and instance.processing_status == GeneStatus.PENDING
        ):
            instance.location = location
            __ = GeneActivity.objects.create(
                type=GeneActivityType.SEND_TO_HANOI_LAB,
                gene_sample_id=instance.id,
                attempts=1,
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data,
                status=status.HTTP_200_OK,
            )
        if location == GeneLocation.GENETICA and (
            (
                instance.location == GeneLocation.HANOI_LAB
                and instance.processing_status == GeneStatus.VERIFIED
            )
            or (
                instance.location == GeneLocation.USA_LAB
                and instance.processing_status == GeneStatus.DECODED
            )
        ):
            instance.location = location
            __ = GeneActivity.objects.create(
                type=GeneActivityType.SEND_TO_GENETICA,
                gene_sample_id=instance.id,
                attempts=1,
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data,
                status=status.HTTP_200_OK,
            )
        if (
            location == GeneLocation.SHIPPING_DEPARTMENT
            and instance.location == GeneLocation.GENETICA
            and instance.processing_status == GeneStatus.PACKAGED
        ):
            instance.location = location
            __ = GeneActivity.objects.create(
                type=GeneActivityType.SEND_TO_SHIPPING,
                gene_sample_id=instance.id,
                attempts=1,
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data,
                status=status.HTTP_200_OK,
            )

        if (
            location == GeneLocation.USA_LAB
            and instance.location == GeneLocation.SHIPPING_DEPARTMENT
            and instance.processing_status == GeneStatus.PACKAGED
        ):
            instance.location = location
            __ = GeneActivity.objects.create(
                type=GeneActivityType.SEND_TO_USA_LAB,
                gene_sample_id=instance.id,
                attempts=1,
            )
            instance.save()
            return Response(
                data=GeneSerializer(instance).data,
                status=status.HTTP_200_OK,
            )

        return Response(
            data="Gene sample' status is not suitable for send",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["put"])
    def cancel(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.last_activity and instance.last_activity.attemps == 2:
            instance.processing_status = GeneStatus.CANCELED
            instance.save()
            return Response(
                data=GeneSerializer(instance).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data="Last activity of this sample is not attemps 2 times",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["post"])
    def activity(self, request, *args, **kwargs):
        instance = self.get_object()
        activity_type = request.data["activity_type"]
        if instance.last_activity and instance.last_activity.type == activity_type:
            instance.last_activity.attempts = 2
        else:
            __ = GeneActivity.objects.create(
                type=activity_type, gene_sample_id=instance.id, attempts=1
            )
        instance.save()
        return Response(
            data=GeneSerializer(instance).data,
            status=status.HTTP_200_OK,
        )
