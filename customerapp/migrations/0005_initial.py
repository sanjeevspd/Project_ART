# Generated by Django 4.2.4 on 2023-10-14 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerapp', '0004_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('email', models.EmailField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'FeedBack',
            },
        ),
    ]
