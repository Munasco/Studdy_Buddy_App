# Generated by Django 3.2.9 on 2021-11-21 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_avatar_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
