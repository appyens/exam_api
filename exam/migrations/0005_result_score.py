# Generated by Django 2.2.14 on 2020-12-26 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20201226_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
