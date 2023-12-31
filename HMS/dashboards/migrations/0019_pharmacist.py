# Generated by Django 4.1.3 on 2023-06-29 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0018_remove_nursespage_name_doctorpage_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_strips2', models.IntegerField()),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='dashboards.doctorpage')),
                ('drugs_assigned2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drugs_assigned2', to='dashboards.doctorpage')),
            ],
        ),
    ]
