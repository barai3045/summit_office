# Generated by Django 4.2.7 on 2023-11-27 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0041_alter_termtext_options_alter_partitem_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentNoteApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.approval')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.paymentnote')),
            ],
        ),
    ]
