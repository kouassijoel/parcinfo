# Generated by Django 4.1.7 on 2023-04-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0038_alter_attribution_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribution',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
