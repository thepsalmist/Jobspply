# Generated by Django 3.0.1 on 2020-03-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20200318_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
