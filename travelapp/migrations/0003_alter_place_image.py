# Generated by Django 4.2.3 on 2023-10-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='gal'),
        ),
    ]