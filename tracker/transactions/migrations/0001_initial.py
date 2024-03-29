# Generated by Django 4.0.1 on 2022-01-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(unique=True)),
                ('brief_description', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.FloatField(default=0.0)),
                ('transaction_type', models.IntegerField(choices=[(1, 'DEBIT'), (2, 'CREDIT')], default=1)),
                ('classification', models.CharField(default='Utility', max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
