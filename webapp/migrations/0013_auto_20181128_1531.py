# Generated by Django 2.1.3 on 2018-11-28 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20181128_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theater',
            old_name='row',
            new_name='rows',
        ),
    ]
