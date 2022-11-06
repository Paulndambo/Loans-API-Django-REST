# Generated by Django 4.1.1 on 2022-11-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('in_grace_period', 'In Grace Period'), ('still_paying', 'Still Paying'), ('fully_paid', 'Full Paid'), ('default_pending', 'Default Pending'), ('defaulted', 'Defaulted')], default='in_grace_period', max_length=255),
        ),
    ]