# Generated by Django 4.2.17 on 2024-12-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
