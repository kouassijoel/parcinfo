# Generated by Django 4.1.7 on 2023-03-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0018_alter_materiel_processeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
