# Generated by Django 4.0.4 on 2022-09-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0005_company_site_department_company_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]