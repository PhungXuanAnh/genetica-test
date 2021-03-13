from rest_framework import serializers
from music.models import Musician, Album, Instrument, Profile


class AlbumModelSerializerReadEffective(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class InstrumentsModelSerializerReadEffective(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']


class MusicianModelSerializerReadEffective_SourceKeyword(serializers.ModelSerializer):
    new_first_name = serializers.CharField(source="first_name")
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    street = serializers.CharField(source="profile.street")
    city = serializers.CharField(source="profile.city")
    full_address = serializers.CharField(source="profile.get_full_address", read_only=True)
    all_albums = AlbumModelSerializerReadEffective(source='album_set', many=True, read_only=True)
    instruments = InstrumentsModelSerializerReadEffective(many=True)

    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        if value.isalnum():
            raise serializers.ValidationError('password must have atleast one special character.')
        return value

    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError("first_name and last_name shouldn't be same.")
        return data

    def to_internal_value(self, data):
        if 'user' in data:
            user_data = data['user']
            return super().to_internal_value(user_data)
        return super().to_internal_value(data)

    def create(self, validated_data):
        # do something else or just call below default statement
        instruments = validated_data.get('instruments', [])
        validated_data.pop('instruments', None)
        musican = Musician.objects.create(**validated_data)
        musican.instruments.set(instruments)
        return musican

    class Meta:
        model = Musician
        fields = [
            "id",
            "new_first_name",
            "last_name",
            "full_name",
            "street",
            "city",
            "full_address",
            'all_albums',
            'instruments',
            'password',
            'profile'
        ]




class ProfileModelSerializerReadEffective(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'street', 'city', 'num_stars']

class MusicianModelSerializerReadEffective_SerializerMethod(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    instruments = serializers.SerializerMethodField()
    profile = ProfileModelSerializerReadEffective()

    def get_instruments(self, obj):
        instruments = obj.instruments.all()
        if not instruments:
            return None
        return InstrumentsModelSerializerReadEffective(instruments, many=True).data

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_full_name(self, obj):
        return obj.get_full_name().upper()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id == 1:
            representation['note'] = 'this is the first record'
        return representation

    def create(self, validated_data):
        profile_data = validated_data.get('profile')
        musican = Musician.objects.create(**validated_data)
        
        profile_data['musician'] = musican
        Profile.objects.create(**profile_data)
        return musican

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            'full_name',
            'instruments', 
            'profile'
        ]

