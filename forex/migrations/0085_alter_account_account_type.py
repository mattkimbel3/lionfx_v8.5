# Generated by Django 3.2.16 on 2023-11-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0084_alter_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('DEMO', 'Demo Account'), ('LIVE', 'Live Account'), ('WALLET', 'Wallet Account')], default='DEMO', max_length=7),
        ),
    ]
