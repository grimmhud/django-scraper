# Generated by Django 4.0 on 2021-12-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebScraping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.TextField()),
                ('website', models.URLField()),
            ],
        ),
    ]
