# Generated by Django 4.1.3 on 2023-06-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0011_alter_checkin_check_in_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='check_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
