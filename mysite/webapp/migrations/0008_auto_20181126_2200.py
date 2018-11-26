# Generated by Django 2.1.3 on 2018-11-26 22:00

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_booker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='seat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Booker')), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D5'), ('D6', 'D6'), ('D7', 'D7'), ('D8', 'D8'), ('D9', 'D9'), ('D10', 'D10'), ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E5'), ('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8'), ('E9', 'E9'), ('E10', 'E10')], max_length=139, null=True),
        ),
    ]
