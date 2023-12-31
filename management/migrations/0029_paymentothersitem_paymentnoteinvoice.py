# Generated by Django 4.2.7 on 2023-11-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0028_paymentothers_paymentnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentOthersItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.DecimalField(decimal_places=0, default=1, max_digits=10)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('vat', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('ait', models.DecimalField(decimal_places=3, default=5.0, max_digits=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.partitem')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.paymentothers')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentNoteInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('particular', models.TextField(max_length=350)),
                ('amount', models.FloatField(default=0.0, max_length=13)),
                ('remark', models.CharField(blank=True, max_length=250, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.paymentnote')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.vendor')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
