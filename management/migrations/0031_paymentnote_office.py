# Generated by Django 4.2.7 on 2023-11-11 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0030_purchaseorder_alter_paymentnoteinvoice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentnote',
            name='office',
            field=models.ForeignKey(default=101, on_delete=django.db.models.deletion.CASCADE, to='management.office'),
        ),
    ]
