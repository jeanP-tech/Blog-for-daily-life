# Generated by Django 2.2.9 on 2020-01-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200123_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='secret',
            field=models.BooleanField(default=False),
        ),
    ]