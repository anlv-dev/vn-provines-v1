# Generated by Django 4.0.4 on 2022-09-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0008_relationshipperson_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='nguoi_than',
        ),
        migrations.AddField(
            model_name='person',
            name='nguoi_than',
            field=models.ManyToManyField(to='province.relationshipperson'),
        ),
    ]
