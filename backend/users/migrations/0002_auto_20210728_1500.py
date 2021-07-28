# Generated by Django 3.2.5 on 2021-07-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='congratulations_after_test',
            field=models.BooleanField(default=False, verbose_name='Был показан экрана поздравления после прохождения теста'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='number_foto_history_by_felling',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер фото истории по ощущениям'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='partner_type',
            field=models.CharField(blank=True, choices=[('GM', 'Для гостевого брака'), ('FAM', 'Для создания семьи'), ('JFF', 'Для просто поболтать и вместе потусить')], max_length=120, null=True, verbose_name='Ищу партнера'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='purpose_meet',
            field=models.CharField(blank=True, choices=[('SAME', 'Такого, как я'), ('ANTI', 'Мою противоположность'), ('MATH', 'Выбор путем математического алгоритма')], max_length=120, null=True, verbose_name='Хочу встретить'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='test_result_demo',
            field=models.CharField(choices=[('NFNP', 'Не найдены, пользователь не оплатил'), ('NFP', 'Не найдены, пользователь оплатил'), ('FNP', 'Найдены, пользователь не оплатил'), ('FP', 'Найдены, пользователь оплатил')], default='NFNP', max_length=4, verbose_name='Демонстрация результатов прохождения теста'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='test_status',
            field=models.CharField(choices=[('start', 'Тестирование не начато'), ('inprogress', 'Тестирование в процессе'), ('finish', 'Тестирование завершено')], default='start', max_length=10, verbose_name='Статус прохождения теста'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='watch_on_boarding',
            field=models.BooleanField(default=False, verbose_name='Статус просмотра on-boarding'),
        ),
    ]
