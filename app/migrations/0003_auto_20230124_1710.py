# Generated by Django 3.2.15 on 2023-01-24 16:10

import app.models.projects
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230112_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='deadline',
        ),
        migrations.AddField(
            model_name='order',
            name='completed_extras',
            field=models.BooleanField(default=False, help_text='Ukończone dodatki', verbose_name='Ukończone dodatki'),
        ),
        migrations.AddField(
            model_name='order',
            name='completed_invitations',
            field=models.BooleanField(default=False, help_text='Ukończone zaproszenia', verbose_name='Ukończone zaproszenia'),
        ),
        migrations.AddField(
            model_name='order',
            name='deadline_extras',
            field=models.DateField(blank=True, help_text='Deadline dodatki', null=True, verbose_name='Deadline dodatki'),
        ),
        migrations.AddField(
            model_name='order',
            name='deadline_invitations',
            field=models.DateField(blank=True, help_text='Deadline zaproszenia', null=True, verbose_name='Deadline zaproszenia'),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, help_text='Adres email', max_length=254, null=True, verbose_name='adres email'),
        ),
        migrations.AddField(
            model_name='order',
            name='file',
            field=models.FileField(blank=True, help_text='Pliki', null=True, upload_to=app.models.projects.request_upload_path, verbose_name='Pliki'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, help_text='Kontaktowy nr telefonu w formacie 123456789', max_length=9, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{9,15}$')], verbose_name='nr telefonu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='stage',
            field=models.ForeignKey(blank=True, help_text='Etap wykonania zlecenia', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stage', verbose_name='Etap'),
        ),
    ]
