# Generated by Django 4.2.2 on 2024-07-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='when',
            field=models.TimeField(blank=True, null=True, verbose_name='время'),
        ),
    ]
