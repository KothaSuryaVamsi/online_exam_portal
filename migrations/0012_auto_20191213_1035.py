# Generated by Django 2.2.4 on 2019-12-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0011_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]
