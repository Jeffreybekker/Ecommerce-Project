# Generated by Django 5.1 on 2024-08-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='invoice_no',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
