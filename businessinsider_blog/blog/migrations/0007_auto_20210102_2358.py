# Generated by Django 3.1.2 on 2021-01-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210102_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
