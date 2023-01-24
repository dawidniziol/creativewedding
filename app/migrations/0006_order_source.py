# Generated by Django 3.2.15 on 2023-01-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.CharField(blank=True, choices=[('INTERNET', 'Z Internetu'), ('OFFICE', 'Z Pracowni'), ('EXHIBITION', 'Z Targów')], help_text='Źródło', max_length=100, null=True, verbose_name='Źródło'),
        ),
    ]