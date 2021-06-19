# Generated by Django 3.2.4 on 2021-06-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_month', models.CharField(max_length=10)),
                ('date_day', models.IntegerField()),
                ('date_year', models.IntegerField()),
                ('date_content', models.CharField(max_length=1000)),
            ],
        ),
    ]
