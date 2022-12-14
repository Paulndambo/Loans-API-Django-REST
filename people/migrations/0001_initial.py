# Generated by Django 4.1.1 on 2022-11-05 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('kra_pin', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('binary', 'Binary'), ('other', 'Other')], max_length=255)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=255)),
                ('birth_date', models.DateField()),
                ('employment', models.JSONField(blank=True, null=True)),
                ('education', models.JSONField(blank=True, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('kra_pin', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('binary', 'Binary'), ('other', 'Other')], max_length=255)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=255)),
                ('birth_date', models.DateField()),
                ('relationship', models.CharField(choices=[('brother_sister', 'Brother/Sister'), ('mother_father', 'Mother/Father'), ('cousin', 'Cousin'), ('aunt_uncle', 'Aunt/Uncle'), ('friend', 'Friend'), ('grandparent', 'Grand Parent')], max_length=255)),
                ('employment', models.JSONField(blank=True, null=True)),
                ('education', models.JSONField(blank=True, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guarantors', to='people.borrower')),
            ],
        ),
    ]
