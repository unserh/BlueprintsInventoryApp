# Generated by Django 3.0.6 on 2020-06-30 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200630_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='director',
        ),
    ]
