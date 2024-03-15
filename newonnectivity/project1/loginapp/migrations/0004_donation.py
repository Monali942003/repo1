# Generated by Django 5.0.2 on 2024-03-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_remove_registration_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=6, null=True)),
                ('amount', models.IntegerField()),
                ('paymentmethod', models.CharField(max_length=10)),
            ],
        ),
    ]
