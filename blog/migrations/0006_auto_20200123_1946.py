# Generated by Django 2.2.9 on 2020-01-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200123_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='id',
            new_name='postId',
        ),
    ]
