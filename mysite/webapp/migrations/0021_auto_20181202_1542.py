# Generated by Django 2.1.3 on 2018-12-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20181202_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='showtimes',
            field=models.CharField(default='10:40,12:10,13:30,14:40,16:30,17:50', max_length=50),
        ),
    ]
