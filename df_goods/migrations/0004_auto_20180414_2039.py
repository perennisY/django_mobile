# Generated by Django 2.0 on 2018-04-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20180414_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default='0'),
        ),
    ]