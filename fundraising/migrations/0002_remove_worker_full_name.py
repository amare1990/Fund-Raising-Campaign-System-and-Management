# Generated by Django 2.2.7 on 2022-01-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='full_name',
        ),
    ]