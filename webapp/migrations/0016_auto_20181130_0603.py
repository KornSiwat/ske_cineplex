# Generated by Django 2.1.3 on 2018-11-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20181129_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='booked_seat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]