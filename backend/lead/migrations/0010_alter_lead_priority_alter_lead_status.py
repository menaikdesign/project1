# Generated by Django 4.2.4 on 2023-09-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0009_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'medium'), ('low', 'low'), ('high', 'high')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('won', 'won'), ('inprogress', 'inprogress'), ('contacted', 'contacted'), ('new', 'new'), ('lost', 'lost')], default='new', max_length=25),
        ),
    ]
