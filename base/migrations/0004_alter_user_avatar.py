# Generated by Django 3.2.9 on 2021-11-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatr.svg', null=True, upload_to=''),
        ),
    ]
