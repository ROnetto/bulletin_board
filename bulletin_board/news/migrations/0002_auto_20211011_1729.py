# Generated by Django 3.1.7 on 2021-10-11 17:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20211008_1845'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('expiration_date', models.DateField(verbose_name='expiration date')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='communities.community', verbose_name='building')),
            ],
            options={
                'verbose_name': 'Building news',
                'verbose_name_plural': 'Building news',
            },
        ),
        migrations.CreateModel(
            name='CommunityNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('expiration_date', models.DateField(verbose_name='expiration date')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='communities.community', verbose_name='community')),
            ],
            options={
                'verbose_name': 'Community news',
                'verbose_name_plural': 'Community news',
            },
        ),
        migrations.RemoveField(
            model_name='communitybulletinboard',
            name='community',
        ),
        migrations.DeleteModel(
            name='BuildingBulletinBoard',
        ),
        migrations.DeleteModel(
            name='CommunityBulletinBoard',
        ),
    ]
