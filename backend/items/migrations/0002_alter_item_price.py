# Generated by Django 3.2 on 2023-12-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]