# Generated by Django 2.2.4 on 2019-09-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0005_registration1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='clgname',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='year',
        ),
    ]
