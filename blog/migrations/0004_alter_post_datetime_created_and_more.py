# Generated by Django 5.0.4 on 2024-05-03 08:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime_modified',
            field=models.DateField(auto_now=True),
        ),
    ]