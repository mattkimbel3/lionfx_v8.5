# Generated by Django 3.2.16 on 2023-08-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0003_alter_forexpair_chart_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forexpair',
            name='chart_data',
            field=models.TextField(),
        ),
    ]
