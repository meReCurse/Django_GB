# Generated by Django 2.1.5 on 2019-02-05 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20190130_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 14, 19, 46, 218205, tzinfo=utc), null=True),
        ),
    ]
