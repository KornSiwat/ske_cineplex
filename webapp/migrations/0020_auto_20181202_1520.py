# Generated by Django 2.1.3 on 2018-12-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_remove_theater_booked_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='first_show',
            field=models.CharField(default='10:40', max_length=50),
        ),
        migrations.AddField(
            model_name='theater',
            name='showtimes',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ticketbooker',
            name='showtime',
            field=models.CharField(default='10:40', max_length=10),
        ),
    ]
