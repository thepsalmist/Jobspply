# Generated by Django 3.0.1 on 2021-02-03 12:04

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_job_apply'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='job',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('pulished', 'Published')], default='draft', max_length=10),
        ),
    ]
