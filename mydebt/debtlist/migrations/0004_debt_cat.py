# Generated by Django 4.1.7 on 2023-04-21 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debtlist', '0003_moneygiver_alter_debt_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='debtlist.moneygiver'),
        ),
    ]