# Generated by Django 3.0 on 2021-04-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210418_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.FloatField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200),
        ),
    ]
