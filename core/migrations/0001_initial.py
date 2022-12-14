# Generated by Django 4.1.1 on 2022-10-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('grace_period', models.IntegerField()),
                ('days_to_repay', models.IntegerField()),
                ('number_of_guarantors', models.IntegerField(default=0)),
                ('minimum_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maximum_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
