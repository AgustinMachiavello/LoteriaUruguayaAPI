# Generated by Django 2.2.5 on 2019-09-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190925_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_administrator',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
