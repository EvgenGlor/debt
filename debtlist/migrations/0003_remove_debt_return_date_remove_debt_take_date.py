# Generated by Django 4.1.7 on 2023-05-03 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debtlist', '0002_alter_debt_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='debt',
            name='take_date',
        ),
    ]