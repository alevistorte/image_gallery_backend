from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Image(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='images', to_field='name')
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
