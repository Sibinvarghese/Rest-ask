# Generated by Django 3.1.3 on 2021-03-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=120)),
                ('Lastname', models.CharField(max_length=120)),
                ('Email_address', models.CharField(max_length=120)),
                ('Password', models.CharField(max_length=12)),
                ('Role', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=10)),
            ],
        ),
    ]
