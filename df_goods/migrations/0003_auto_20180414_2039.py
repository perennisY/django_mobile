# Generated by Django 2.0 on 2018-04-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180407_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
