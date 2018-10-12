# Generated by Django 2.0.9 on 2018-10-05 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('project', models.CharField(blank=True, max_length=200, null=True)),
                ('config', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('DB', 'DB'), ('SERVER', 'Server'), ('GENERAL', 'General')], default='GENERAL', max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]