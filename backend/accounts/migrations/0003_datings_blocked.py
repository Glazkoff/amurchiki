# Generated by Django 3.2.5 on 2021-07-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210709_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='datings',
            name='blocked',
            field=models.BooleanField(default=False, verbose_name='Совпадение было заблокировано пользователем'),
        ),
    ]
