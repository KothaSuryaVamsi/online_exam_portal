# Generated by Django 2.2.4 on 2019-09-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0003_remove_registration_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='emailid',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
