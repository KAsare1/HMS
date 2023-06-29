# Generated by Django 4.1.3 on 2023-06-28 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboards', '0014_alter_checkin_doctorassigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='DoctorAssigned',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups': '8'}, max_length=30, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboards.registrationpage'),
        ),
    ]
