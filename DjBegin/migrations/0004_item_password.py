# Generated by Django 3.2.6 on 2021-08-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjBegin', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
