# Generated by Django 2.1.5 on 2019-02-20 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0042_auto_20190220_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 12, 8, 3, 562211, tzinfo=utc), null=True),
        ),
    ]
