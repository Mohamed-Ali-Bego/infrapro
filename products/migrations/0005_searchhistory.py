# Generated by Django 4.2.16 on 2024-11-15 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_is_active_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('puplish_date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['puplish_date'],
            },
        ),
    ]
