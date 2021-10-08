# Generated by Django 3.1.7 on 2021-03-10 22:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingFloor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buildings.building', verbose_name='building')),
            ],
            options={
                'verbose_name': 'Building floor',
                'verbose_name_plural': 'Building floors',
            },
        ),
    ]