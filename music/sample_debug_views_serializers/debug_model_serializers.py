import debugpy
from rest_framework import serializers
from music.models import Musician

class MusicianModelDebugSerializer(serializers.ModelSerializer):
    # NOTE: SerializerMethodField is read only field
    # so just using with get/list Serializer
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = Musician
        fields = ['id', 'first_name', 'last_name', 'instruments']

    def to_internal_value(self, data):
        debugpy.breakpoint()
        return super().to_internal_value(data)

    def validate_first_name(self, value):
        # NOTE: this method will be ignore
        # if declare first_name = serializers.SerializerMethodField()
        # above, because it become read only field from model
        debugpy.breakpoint()
        return value

    def validate_last_name(self, value):
        debugpy.breakpoint()
        return value

    def validate(self, attrs):
        debugpy.breakpoint()
        return super().validate(attrs)

    def create(self, validated_data):
        debugpy.breakpoint()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        debugpy.breakpoint()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        debugpy.breakpoint()
        return super().to_representation(instance)

    def get_first_name(self, obj):
        # NOTE: to using this method
        # it must be declare first_name = serializers.SerializerMethodField()
        # above, and just using inside Serializer for get/list method
        # if using with put/post this field will be ignored
        debugpy.breakpoint()
        if obj.first_name == "first_name 1":
            return "new first name 1"
        else:
            return "new first name 2" 
