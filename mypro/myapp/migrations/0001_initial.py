# Generated by Django 3.1.1 on 2023-04-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_ID', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]