# Generated by Django 3.2.16 on 2023-08-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0015_alter_optiontrade_stake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optiontrade',
            name='stake',
        ),
    ]
