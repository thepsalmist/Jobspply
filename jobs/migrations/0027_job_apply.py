# Generated by Django 3.0.1 on 2021-03-10 07:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0026_remove_job_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]