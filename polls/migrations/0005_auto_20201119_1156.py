# Generated by Django 2.2.10 on 2020-11-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201119_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
