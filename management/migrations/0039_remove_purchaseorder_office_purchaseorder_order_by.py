# Generated by Django 4.2.7 on 2023-11-20 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_rename_title_s_title_stitle'),
        ('management', '0038_approval_raise_by_approval_submitted_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='office',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='order_by',
            field=models.ForeignKey(default='99078', on_delete=django.db.models.deletion.CASCADE, to='hr.employee'),
        ),
    ]
