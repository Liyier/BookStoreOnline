# Generated by Django 2.0.5 on 2018-06-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0011_auto_20180608_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.RemoveField(
            model_name='books',
            name='add_time',
        ),
    ]
