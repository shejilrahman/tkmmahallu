# Generated by Django 4.0.7 on 2022-12-18 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='user',
        ),
    ]