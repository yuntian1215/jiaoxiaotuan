# Generated by Django 3.2.13 on 2022-05-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanzi', '0005_auto_20220503_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
