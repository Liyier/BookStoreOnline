# Generated by Django 2.0.5 on 2018-06-07 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0005_auto_20180607_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='head_portrait',
        ),
    ]