# Generated by Django 5.2 on 2025-04-14 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_created_at_post_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
    ]
