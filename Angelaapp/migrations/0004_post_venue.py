# Generated by Django 4.1.7 on 2023-04-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Angelaapp', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Text', models.Field(max_length=50)),
                ('CreatedDate', models.DateTimeField()),
                ('PublishedDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VenueName', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('ZipPostCode', models.IntegerField()),
                ('ContactPhone', models.IntegerField()),
                ('WebAddress', models.CharField(max_length=50)),
                ('EmailAddress', models.EmailField(max_length=254)),
            ],
        ),
    ]