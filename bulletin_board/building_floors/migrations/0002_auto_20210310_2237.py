# Generated by Django 3.1.7 on 2021-03-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_floors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingfloor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
