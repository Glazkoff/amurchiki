# Generated by Django 3.2.6 on 2021-08-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_alter_groupquestion_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupquestion',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Прядок'),
        ),
    ]
