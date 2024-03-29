# Generated by Django 3.0.1 on 2021-02-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20210221_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('sales & marketing', 'Sales/Marketting'), ('accounting & finance', 'Accounting/Finance'), ('software engineering', 'Software/Engineering'), ('ict & telecommunications', 'ICT/Telecommunications'), ('manufacturing & production', 'Manufacturing/Production'), ('ngo', 'NGO'), ('education & teaching', 'Education/Teaching'), ('media & social_media', 'Media/Social_Media'), ('healthcare & medical', 'Healthcare/Medical')], max_length=256),
        ),
    ]
