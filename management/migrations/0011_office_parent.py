# Generated by Django 4.2.7 on 2023-11-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_alter_office_contact_alter_office_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='parent',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
