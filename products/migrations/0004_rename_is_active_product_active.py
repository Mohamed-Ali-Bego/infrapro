# Generated by Django 4.2.16 on 2024-11-06 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_options_category_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_active',
            new_name='active',
        ),
    ]
