# Generated by Django 4.2.11 on 2024-04-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_advert_images'),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
