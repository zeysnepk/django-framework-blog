# Generated by Django 5.0.7 on 2024-08-05 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_username',
            new_name='comment_name',
        ),
    ]
