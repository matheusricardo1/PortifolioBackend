# Generated by Django 5.1.1 on 2024-12-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_service_options_service_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]