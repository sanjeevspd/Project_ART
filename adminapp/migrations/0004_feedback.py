# Generated by Django 4.2.4 on 2023-10-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_delete_adminpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'FeedBack',
            },
        ),
    ]
