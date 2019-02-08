# Generated by Django 2.1.5 on 2019-02-06 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0021_auto_20190206_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 9, 19, 39, 4271, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='language',
            field=models.TextField(blank=True, verbose_name='язык'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='url',
            field=models.URLField(blank=True, verbose_name='url'),
        ),
    ]
