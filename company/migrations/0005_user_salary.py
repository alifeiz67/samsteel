# Generated by Django 4.0.2 on 2022-06-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
