# Generated by Django 2.2.10 on 2020-11-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20201119_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Результаты'),
        ),
    ]
