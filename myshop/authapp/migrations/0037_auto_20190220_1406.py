# Generated by Django 2.1.5 on 2019-02-20 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0036_auto_20190220_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 11, 6, 55, 86417, tzinfo=utc), null=True),
        ),
    ]
