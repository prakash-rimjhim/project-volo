# Generated by Django 4.1.7 on 2023-06-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('Software', models.CharField(max_length=50)),
                ('seats', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
