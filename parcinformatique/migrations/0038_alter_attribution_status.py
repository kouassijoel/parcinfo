# Generated by Django 4.1.7 on 2023-04-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0037_attribution_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribution',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]