# Generated by Django 3.2 on 2022-12-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_member_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]