# Generated by Django 4.1.6 on 2023-10-03 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(max_length=6),
        ),
    ]
