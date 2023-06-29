# Generated by Django 4.1.3 on 2023-06-28 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboards', '0006_alter_appointment_name_checkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='DoctorAssigned',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups': '8'}, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]