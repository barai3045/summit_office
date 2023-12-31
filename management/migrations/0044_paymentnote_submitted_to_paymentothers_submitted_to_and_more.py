# Generated by Django 4.2.7 on 2023-12-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_rename_title_s_title_stitle'),
        ('management', '0043_remove_paymentnote_office_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentnote',
            name='submitted_to',
            field=models.ForeignKey(default='99090', on_delete=django.db.models.deletion.CASCADE, related_name='payment_submiited_to', to='hr.employee'),
        ),
        migrations.AddField(
            model_name='paymentothers',
            name='submitted_to',
            field=models.ForeignKey(default='99090', on_delete=django.db.models.deletion.CASCADE, related_name='others_submiited_to', to='hr.employee'),
        ),
        migrations.AlterField(
            model_name='paymentnote',
            name='raise_by',
            field=models.ForeignKey(default='99078', on_delete=django.db.models.deletion.CASCADE, related_name='payment_raised_by', to='hr.employee'),
        ),
        migrations.AlterField(
            model_name='paymentothers',
            name='raise_by',
            field=models.ForeignKey(default='99078', on_delete=django.db.models.deletion.CASCADE, related_name='others_raised_by', to='hr.employee'),
        ),
    ]
