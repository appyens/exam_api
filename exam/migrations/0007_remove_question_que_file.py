# Generated by Django 2.2.14 on 2020-12-26 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20201226_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='que_file',
        ),
    ]
