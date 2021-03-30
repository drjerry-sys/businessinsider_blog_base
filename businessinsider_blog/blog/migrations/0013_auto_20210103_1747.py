# Generated by Django 3.1.2 on 2021-01-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210103_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='popular',
            field=models.CharField(choices=[('news', 'NEWS'), ('trending', 'TRENDING'), ('local', 'LOCAL'), ('retail', 'RETAIL')], default='news', max_length=10),
        ),
    ]