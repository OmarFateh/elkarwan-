# Generated by Django 3.0.8 on 2020-08-16 22:40

from django.db import migrations
import django_resized.forms
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200816_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[160, 160], upload_to=product.models.product_image_upload_to),
        ),
    ]
