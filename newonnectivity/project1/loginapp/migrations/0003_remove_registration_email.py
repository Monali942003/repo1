# Generated by Django 5.0.2 on 2024-03-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_registration_alter_login_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Email',
        ),
    ]
