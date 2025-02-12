# Generated by Django 5.1.3 on 2025-01-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_exchange_cur_date_alter_exchange_cur_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='cur_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='날짜'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='cur_unit',
            field=models.CharField(db_index=True, max_length=10, verbose_name='화폐 단위'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='deal_bas_r',
            field=models.FloatField(verbose_name='현재 환율'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='ttb',
            field=models.FloatField(default=0.0, verbose_name='사실 때'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='tts',
            field=models.FloatField(default=0.0, verbose_name='파실 때'),
        ),
    ]
