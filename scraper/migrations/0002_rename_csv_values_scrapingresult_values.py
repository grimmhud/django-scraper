# Generated by Django 4.0 on 2022-01-08 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapingresult',
            old_name='csv_values',
            new_name='values',
        ),
    ]
