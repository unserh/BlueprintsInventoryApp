# Generated by Django 3.0.6 on 2020-07-01 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20200701_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='chapter',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='login.Chapter'),
            preserve_default=False,
        ),
    ]
