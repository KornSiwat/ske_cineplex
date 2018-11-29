# Generated by Django 2.1.3 on 2018-11-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20181126_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='seat',
        ),
        migrations.AddField(
            model_name='theater',
            name='booked_seat',
            field=models.TextField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='theater',
            name='row',
            field=models.PositiveIntegerField(default=9),
        ),
        migrations.AddField(
            model_name='theater',
            name='seats',
            field=models.PositiveIntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='movie',
            name='categorie',
            field=models.CharField(choices=[('GE', 'General'), ('AC', 'Action'), ('AD', 'Adults'), ('AV', 'Adventure'), ('FS', 'Fantasy'), ('HR', 'Horror'), ('KD', 'Kids')], default='GE', max_length=2),
        ),
    ]