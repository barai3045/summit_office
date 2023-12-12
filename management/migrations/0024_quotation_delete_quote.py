# Generated by Django 4.2.7 on 2023-11-11 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_alter_termtext_options_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('reference', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField()),
                ('advance_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('security_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('vat_deducted', models.BooleanField(default=False)),
                ('ait_deducted', models.BooleanField(default=True)),
                ('selected', models.BooleanField(default=True)),
                ('approval', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.approval')),
                ('contact', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.vendorcontact')),
                ('item_type', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='management.itemtype')),
            ],
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]