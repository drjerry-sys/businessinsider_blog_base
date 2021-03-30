# Generated by Django 3.1.2 on 2021-01-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210103_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='popular',
            field=models.CharField(choices=[('news', 'NEWS'), ('trending', 'TRENDING')], default='news', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique_for_date='category'),
        ),
    ]
