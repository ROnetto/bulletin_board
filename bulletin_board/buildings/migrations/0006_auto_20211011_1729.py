# Generated by Django 3.1.7 on 2021-10-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0005_auto_20211008_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='type',
            field=models.IntegerField(choices=[(0, 'House'), (1, 'Apartment building')], default=0, verbose_name='type'),
        ),
    ]
