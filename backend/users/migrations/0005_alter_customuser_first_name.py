# Generated by Django 3.2.4 on 2021-06-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='Администратор', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
