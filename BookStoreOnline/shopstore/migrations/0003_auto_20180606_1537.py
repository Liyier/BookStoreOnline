# Generated by Django 2.0.5 on 2018-06-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0002_auto_20180606_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='重庆市邮电大学', verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.PositiveIntegerField(default=0, verbose_name='余额'),
        ),
        migrations.AddField(
            model_name='user',
            name='head_portrait',
            field=models.ImageField(default=None, upload_to='', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456', max_length=30, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='电话号码'),
        ),
    ]
