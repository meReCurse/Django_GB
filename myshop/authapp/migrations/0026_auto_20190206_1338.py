# Generated by Django 2.1.5 on 2019-02-06 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0025_auto_20190206_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 10, 38, 54, 560304, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='language',
            field=models.CharField(blank=True, max_length=30, verbose_name='язык'),
        ),
    ]
