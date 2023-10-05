# Generated by Django 4.2.4 on 2023-09-09 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_lead_assigned_to_alter_lead_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('lost', 'lost'), ('won', 'won'), ('inprogress', 'inprogress'), ('new', 'new'), ('contacted', 'contacted')], default='new', max_length=25),
        ),
    ]
