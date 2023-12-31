# Generated by Django 4.2.7 on 2023-11-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_vendoraccount_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('show_payment', models.BooleanField(default=True)),
                ('signed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
