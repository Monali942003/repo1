# Generated by Django 5.0.2 on 2024-03-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_delete_record_registration_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=22, null=True),
        ),
    ]
