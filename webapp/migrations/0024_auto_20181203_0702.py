# Generated by Django 2.1.3 on 2018-12-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_auto_20181202_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
