# Generated by Django 4.2.6 on 2023-11-09 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentences',
            old_name='data_sentence',
            new_name='paragraph',
        ),
    ]