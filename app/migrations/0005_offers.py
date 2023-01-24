# Generated by Django 3.2.15 on 2023-01-24 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order_angels_extras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa zapytania', max_length=250, unique=True, verbose_name='Zapytanie')),
                ('description', models.TextField(blank=True, help_text='Szczegółowy opis zamówienia', verbose_name='Opis')),
                ('email', models.EmailField(blank=True, help_text='Adres email', max_length=254, null=True, verbose_name='adres email')),
                ('phone', models.CharField(blank=True, help_text='Kontaktowy nr telefonu w formacie 123456789', max_length=9, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{9,15}$')], verbose_name='nr telefonu')),
                ('samples', models.BooleanField(default=False, help_text='Próbki', verbose_name='Próbki')),
                ('forms', models.BooleanField(default=False, help_text='Zapytanie z formularza', verbose_name='Zapytanie z formularza')),
            ],
            options={
                'verbose_name': 'zapytanie',
                'verbose_name_plural': 'zapytanie',
                'db_table': 'offer',
            },
        ),
    ]
