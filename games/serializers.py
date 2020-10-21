from rest_framework import serializers
from .models import Games


class GameSerializer(serializers.Serializer):
    """
    serializer for Game model
    """
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    catagory = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)
    release_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Games.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.catagory = validated_data.get('catagory', instance.catagory)
        instance.played = validated_data.get('played', instance.played)
        instance.release_date = validated_data.get('release_date',
                                                   instance.release_date)
        instance.save()
        return instance
