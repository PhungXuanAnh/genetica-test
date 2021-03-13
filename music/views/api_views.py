from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework.exceptions import APIException

from music.models import Musician, Album
from music.serializers.model_serializers import MusicianModelSerializer, InstrumentModelSerializer


class CreateListMusicanView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    # NOTE: don't have paging yet, implement by your self

    def post(self, request, format=None):
        # validated_data = self.validate(request.data)
        # musican = Musician.objects.create(**validated_data)
        # return Response({
        #     "id": musican.id,
        #     "first_name": musican.first_name,
        #     "last_name": musican.last_name,
        #     "instrument": musican.instrument
        # })

        serializer = MusicianModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self, request, format=None):
        # results = []
        # for musican in Musician.objects.all():
        #     results.append({
        #         "id": musican.id,
        #         "first_name": musican.first_name,
        #         "last_name": musican.last_name,
        #         "instrument": musican.instrument
        #     })

        serializer = MusicianModelSerializer(Musician.objects.all(), many=True)
        results = serializer.data

        return Response({
            "count": len(results),
            "next": None,               # NOTE: don't paging yet
            "previous": None,           # NOTE: don't paging yet
            "results": results
        })



    def validate(self, data):
        validated_data = {}

        required_fields = ["first_name", "last_name", "instrument"]
        for key in required_fields:
            if key not in data:
                raise APIException(
                    "Missing field: {}".format(key), status.HTTP_400_BAD_REQUEST
                )
            validated_data[key] = data[key]

        return validated_data


class MusicanRetriveUpdateDestroyView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, id, format=None):
        try:
            musican = Musician.objects.get(id=id)
        except Musician.DoesNotExist:
            raise APIException("Musican not found", status.HTTP_404_NOT_FOUND)

        return Response({
            "id": musican.id,
            "first_name": musican.first_name,
            "last_name": musican.last_name,
            "instruments": [{"id": inst.id, "name": inst.name} for inst in musican.instruments.all()]
        })

    def put(self, request, id, format=None):
        data = request.data
        # validate()

        try:
            musican = Musician.objects.get(id=id)
            musican.first_name = data["first_name"]
            musican.last_name = data["last_name"]
            musican.instruments.set(data["instruments"])
            musican.save()
        except Musician.DoesNotExist:
            raise APIException("Musican not found", status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            raise APIException("Missing field: {}".format(e.args), status.HTTP_400_BAD_REQUEST)

        return Response({
            "id": musican.id,
            "first_name": musican.first_name,
            "last_name": musican.last_name,
            "instruments": [{"id": inst.id, "name": inst.name} for inst in musican.instruments.all()]
        })

    def patch(self, request, id, format=None):
        return Response({})

    def delete(self, request, id, format=None):
        return Response({})

   

class MusicanFullNameView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, id, format=None):
        try:
            musican = Musician.objects.get(id=id)
        except Musician.DoesNotExist:
            raise APIException("Musican not found", status.HTTP_404_NOT_FOUND)

        return Response({
            "full_name": musican.first_name + " " + musican.last_name
        })
