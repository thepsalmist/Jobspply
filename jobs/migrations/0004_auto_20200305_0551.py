# Generated by Django 3.0.1 on 2020-03-05 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('publish',)},
        ),
    ]
