# Generated by Django 2.1.5 on 2019-02-13 16:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0027_auto_20190206_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 14, 19, 532708, tzinfo=utc), null=True),
        ),
    ]
