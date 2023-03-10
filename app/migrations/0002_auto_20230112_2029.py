# Generated by Django 3.2.15 on 2023-01-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, help_text='Szczegółowy opis zamówienia', verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(help_text='Termin wykonania', verbose_name='Deadline'),
        ),
    ]
