# Generated by Django 2.2.15 on 2020-08-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200817_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon_type',
            field=models.CharField(choices=[('tools', 'أدوات'), ('hammer', 'شاكوش'), ('toolbox', 'صندوق أدوات'), ('screwdriver', 'مفك'), ('wrench', 'مفتاح')], max_length=15, verbose_name='Icon'),
        ),
    ]
