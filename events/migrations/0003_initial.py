# Generated by Django 4.2.18 on 2025-03-03 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
        ),
    ]
