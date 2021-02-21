# Generated by Django 3.0.1 on 2021-02-21 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20210221_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('sales/marketing', 'Sales/Marketting'), ('accounting/finance', 'Accounting/Finance'), ('software/engineering', 'Software/Engineering'), ('ict/telecommunications', 'ICT/Telecommunications'), ('manufacturing/production', 'Manufacturing/Production'), ('ngo', 'NGO'), ('education/teaching', 'Education/Teaching'), ('media/social_media', 'Media/Social_Media'), ('healthcare/medical', 'Healthcare/Medical')], max_length=256)),
                ('slug', models.SlugField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('name',), 'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.AddField(
            model_name='job',
            name='jobcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Category'),
        ),
    ]