# Generated by Django 3.2.18 on 2023-03-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleApp', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]