# Generated by Django 3.0.4 on 2021-02-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250, null=True)),
                ('gender', models.CharField(max_length=250, null=True)),
                ('age', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
