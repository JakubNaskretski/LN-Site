# Generated by Django 2.1.7 on 2019-03-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0005_product_priduct_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
