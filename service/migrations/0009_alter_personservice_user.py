# Generated by Django 5.0.4 on 2024-05-02 17:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_remove_personservice_birth_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='personservice',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_personservice', to=settings.AUTH_USER_MODEL),
        ),
    ]
