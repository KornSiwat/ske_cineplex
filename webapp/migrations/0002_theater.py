# Generated by Django 2.1.3 on 2018-11-23 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_id', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movie')),
            ],
        ),
    ]
