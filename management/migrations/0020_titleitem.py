# Generated by Django 4.2.7 on 2023-11-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_alter_partitem_options_rename_iid_partitem_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleItem',
            fields=[
                ('tid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('item', models.TextField()),
            ],
            options={
                'ordering': ['tid'],
            },
        ),
    ]
