# Generated by Django 3.2.5 on 2021-07-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210709_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='watch_on_boarding',
            field=models.BooleanField(default=False, verbose_name='Статус просмотра on-boarding'),
        ),
    ]
