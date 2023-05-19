# Generated by Django 4.2 on 2023-05-18 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('main', '0002_dataset_tagged_at_dataset_verified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='verifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.verifier'),
        ),
    ]
