# Generated by Django 3.0.1 on 2020-06-03 18:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
