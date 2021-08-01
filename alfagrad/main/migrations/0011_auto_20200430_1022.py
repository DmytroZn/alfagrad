# Generated by Django 3.0.5 on 2020-04-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AddField(
            model_name='baselevel',
            name='first_text',
            field=models.CharField(default='d', max_length=100, verbose_name='первый скрипт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baselevel',
            name='second_text',
            field=models.CharField(default='dd', max_length=100, verbose_name='второй скрипт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baselevel',
            name='third_text',
            field=models.CharField(default='dddd', max_length=100, verbose_name='третий скрипт'),
            preserve_default=False,
        ),
    ]
