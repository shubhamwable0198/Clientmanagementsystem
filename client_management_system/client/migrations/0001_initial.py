# Generated by Django 5.0.7 on 2024-08-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=30)),
                ('date_of_joining', models.DateField()),
                ('status', models.CharField(choices=[('Onboard', 'Onboard'), ('NotOnboard', 'NotOnboard')], max_length=30)),
                ('projectDomain', models.CharField(choices=[('SAAS', 'SAAS'), ('Ecommerce', 'Ecommerce'), ('CRM', 'CRM'), ('ERM', 'ERM'), ('Finance', 'Finance')], max_length=50)),
            ],
        ),
    ]
