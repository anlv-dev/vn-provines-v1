# Generated by Django 4.0.4 on 2022-09-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0009_remove_person_nguoi_than_person_nguoi_than'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Nam'), ('F', 'Nữ'), ('O', 'Khác')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='relationshipperson',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Nam'), ('F', 'Nữ'), ('O', 'Khác')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='relationshipperson',
            name='moi_quan_he',
            field=models.CharField(blank=True, choices=[('BV', 'Ba Vợ'), ('MV', 'Mẹ Vợ'), ('BC', 'Ba Chồng'), ('MC', 'Mẹ Chồng'), ('CO', 'Con')], max_length=20, null=True),
        ),
    ]
