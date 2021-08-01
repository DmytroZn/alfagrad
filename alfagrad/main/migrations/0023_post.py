# Generated by Django 3.0.5 on 2020-05-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_baselevel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
