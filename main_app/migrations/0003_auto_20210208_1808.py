# Generated by Django 3.1.6 on 2021-02-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210208_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='pokedex_no',
            new_name='pokedex_id',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]