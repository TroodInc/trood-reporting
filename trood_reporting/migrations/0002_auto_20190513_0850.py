# Generated by Django 2.2 on 2019-05-13 08:50

from django.db import migrations, models
import trood_reporting.models


class Migration(migrations.Migration):

    dependencies = [
        ('trood_reporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='code',
            field=models.CharField(db_index=True, default=trood_reporting.models.default_uuid, help_text='Code', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='code',
            field=models.CharField(db_index=True, default=trood_reporting.models.default_uuid, help_text='Code', max_length=128, unique=True),
        ),
    ]
