# Generated by Django 3.2.16 on 2023-08-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0028_alter_optiontrade_close_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='optiontrade',
            name='outcome',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
