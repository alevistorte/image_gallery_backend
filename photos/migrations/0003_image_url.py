# Generated by Django 4.2 on 2023-04-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_product_image_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.URLField(default='', max_length=255),
            preserve_default=False,
        ),
    ]