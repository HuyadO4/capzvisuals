# Generated by Django 3.2.7 on 2022-08-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20220807_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=2080),
        ),
    ]