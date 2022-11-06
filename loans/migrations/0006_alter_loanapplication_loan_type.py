# Generated by Django 4.1.1 on 2022-11-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_loantype_interest_rate'),
        ('loans', '0005_alter_loanapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.loantype'),
        ),
    ]