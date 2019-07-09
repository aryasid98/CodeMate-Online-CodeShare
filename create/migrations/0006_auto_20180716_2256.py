# Generated by Django 2.1b1 on 2018-07-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0005_remove_create_code_expire'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_code',
            name='expire',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='create_code',
            name='content',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='create_code',
            name='slug',
            field=models.CharField(max_length=10),
        ),
    ]