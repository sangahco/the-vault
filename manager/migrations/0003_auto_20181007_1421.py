# Generated by Django 2.0.9 on 2018-10-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_secret_config2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='label',
            field=models.CharField(max_length=200),
        ),
    ]
