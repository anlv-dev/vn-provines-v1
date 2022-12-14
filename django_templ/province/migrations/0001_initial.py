# Generated by Django 4.0.4 on 2022-09-07 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('name_with_type', models.CharField(max_length=255)),
                ('code', models.IntegerField()),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('name_with_type', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=500)),
                ('path_with_type', models.CharField(max_length=1000)),
                ('code', models.IntegerField()),
                ('parent_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='province.city')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('name_with_type', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=500)),
                ('path_with_type', models.CharField(max_length=1000)),
                ('code', models.IntegerField()),
                ('parent_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='province.district')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
