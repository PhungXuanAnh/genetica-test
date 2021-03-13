from rest_framework import serializers


class InstrumentsSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)

class MusicianSerializer(serializers.Serializer):
    # NOTE: this serializer is not secify model
    # it must be define field explicitly
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    instruments = InstrumentsSerializer()