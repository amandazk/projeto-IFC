# Generated by Django 3.1.3 on 2020-11-12 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbfone',
            name='pessoa',
        ),
    ]