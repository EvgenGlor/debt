# Generated by Django 4.1.7 on 2023-05-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtlist', '0013_alter_debt_options_alter_moneygiver_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='id',
        ),
        migrations.AlterField(
            model_name='debt',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
