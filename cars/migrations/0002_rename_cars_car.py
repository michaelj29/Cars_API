# Generated by Django 4.0.3 on 2022-03-30 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]
