# Generated by Django 2.1.3 on 2018-12-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20181203_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbooker',
            name='movie',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
