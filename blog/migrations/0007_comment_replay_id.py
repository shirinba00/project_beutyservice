# Generated by Django 5.0.4 on 2024-05-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_is_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replay_id',
            field=models.IntegerField(null=True),
        ),
    ]
