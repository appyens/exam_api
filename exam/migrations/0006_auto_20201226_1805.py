# Generated by Django 2.2.14 on 2020-12-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_result_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
