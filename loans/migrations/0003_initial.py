# Generated by Django 4.1.1 on 2022-11-05 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_loantype_interest_rate'),
        ('people', '0002_guarantor_email'),
        ('loans', '0002_delete_loan_delete_loanapplication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_applied', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_awarded', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_interest', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_to_repay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_repaid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('in_grace_period', 'In Grace Period'), ('still_paying', 'Still Paying'), ('fully_paid', 'Full Paid'), ('default_pending', 'Default Pending'), ('defaulted', 'Defaulted')], max_length=255)),
                ('date_applied', models.DateTimeField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='people.borrower')),
                ('loan_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.loantype')),
            ],
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.JSONField(blank=True, null=True)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_payments', to='people.borrower')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan')),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_applying', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('declined', 'Declined')], max_length=255)),
                ('decline_reason', models.TextField(blank=True, null=True)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_applications', to='people.borrower')),
                ('loan_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.loantype')),
            ],
        ),
    ]
