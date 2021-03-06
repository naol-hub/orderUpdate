# Generated by Django 3.0 on 2021-04-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_order_custom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custom',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
    ]
