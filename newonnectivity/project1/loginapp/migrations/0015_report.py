# Generated by Django 5.0.2 on 2024-03-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0014_record_accidenttype_record_roadfeatures_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('injury', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('area', models.CharField(max_length=10, null=True)),
                ('complain', models.CharField(max_length=80, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('date', models.CharField(max_length=6, null=True)),
                ('description', models.CharField(max_length=34, null=True)),
            ],
        ),
    ]
