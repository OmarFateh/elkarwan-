# Generated by Django 3.0.8 on 2020-08-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_icon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon_type',
            field=models.CharField(choices=[('أدوات', 'أدوات'), ('شاكوش', 'شاكوش'), ('صندوق أدوات', 'صندوق أدوات'), ('مفك', 'ٍمفك'), ('مفتاح', 'مفتاح')], max_length=15),
        ),
    ]