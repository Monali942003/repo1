# Generated by Django 5.0.2 on 2024-03-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0015_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='injury',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
