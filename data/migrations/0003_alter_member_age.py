# Generated by Django 3.2 on 2022-12-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_remove_family_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
