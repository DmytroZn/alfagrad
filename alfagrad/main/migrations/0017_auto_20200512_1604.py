# Generated by Django 3.0.5 on 2020-05-12 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200512_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baselevel',
            options={'verbose_name': 'Правая панель'},
        ),
        migrations.AlterModelOptions(
            name='subtext',
            options={'verbose_name': 'Пункт', 'verbose_name_plural': 'Пункты'},
        ),
    ]
