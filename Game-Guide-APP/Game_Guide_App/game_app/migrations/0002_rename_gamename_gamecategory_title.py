# Generated by Django 5.1.2 on 2024-10-26 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamecategory',
            old_name='gamename',
            new_name='title',
        ),
    ]