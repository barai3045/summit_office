# Generated by Django 4.2.7 on 2023-11-13 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_rename_designation_vendorcontact_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentothersitem',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='quotationitem',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='office',
            field=models.ForeignKey(default='101', on_delete=django.db.models.deletion.CASCADE, to='management.office'),
        ),
    ]
