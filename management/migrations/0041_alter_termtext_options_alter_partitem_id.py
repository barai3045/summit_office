# Generated by Django 4.2.7 on 2023-11-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0040_alter_purchaseorderterm_options_termtext_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='termtext',
            options={'ordering': ['title', 'text']},
        ),
        migrations.AlterField(
            model_name='partitem',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
