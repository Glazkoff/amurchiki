# Generated by Django 3.2.4 on 2021-06-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210623_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Пользователь является сотрудником'),
        ),
    ]