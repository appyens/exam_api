# Generated by Django 2.2.14 on 2020-12-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20201226_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='question',
            name='que_type',
            field=models.CharField(choices=[('helping_others', 'Helping others'), ('communicational', 'Communicational'), ('organizational', 'Organizational')], max_length=30),
        ),
        migrations.AlterField(
            model_name='result',
            name='answer',
            field=models.CharField(choices=[('strongly_agree', 'Strongly agree'), ('agree', 'Agree'), ('neutral', 'Neutral'), ('disagree', 'Disagree'), ('strongly_disagree', 'Strongly Disagree')], max_length=30),
        ),
    ]
