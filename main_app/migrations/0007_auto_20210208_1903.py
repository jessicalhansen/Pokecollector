# Generated by Django 3.1.6 on 2021-02-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210208_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
