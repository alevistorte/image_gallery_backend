from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Image, Collection, Tags
from .serializers import AddImageSerializer, ImageSerializer, CollectionSerializer, CollectionNameSerializer


class ImagesViewSet(ModelViewSet):
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddImageSerializer
        return ImageSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.prefetch_related('images').all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CollectionNameSerializer
        return CollectionSerializer
