from rest_framework import serializers
from .models import Message, Coordinate, Photo_path, Spot, Character, Environment, Access_point, Character_data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text_data')


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('latitude', 'longitude')


class Photo_pathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo_path
        fields = ('photo_file_path')


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('spot_name', 'spot_phoname', 'steet_address', 'postal_code')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('character_name')

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('weather', 'temperature')


class Access_pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_point
        fields = ('raspberry_pi_number', 'access_point_name')


class Character_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_data
        fields = ('character_file_pass')
