# Generated by Django 3.1.7 on 2021-10-11 17:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0003_auto_20211008_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='admins',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='admins'),
        ),
    ]