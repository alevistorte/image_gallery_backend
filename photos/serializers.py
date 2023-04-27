from rest_framework import serializers
from .models import Collection, Image, Tags


class AddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'title', 'collection', 'url']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class CollectionSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = ['name', 'images']
