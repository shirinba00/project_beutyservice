# Generated by Django 5.0.4 on 2024-04-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_typeservice_description_typeservice_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeservice',
            name='info',
            field=models.TextField(),
        ),
    ]
