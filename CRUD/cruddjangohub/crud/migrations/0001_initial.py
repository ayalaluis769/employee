# Generated by Django 3.2.4 on 2021-09-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.TextField()),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_mobile', models.TextField()),
            ],
        ),
    ]
