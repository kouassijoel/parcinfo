# Generated by Django 4.1.7 on 2023-03-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0017_alter_materiel_date_acquisition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='processeur',
            field=models.CharField(choices=[('Celeron', 'Celeron'), ('Core i3', 'Core i3'), ('Core i5', 'Core i5'), ('Core i7', 'Core i7'), ('Core i9', 'Core i9')], max_length=10),
        ),
    ]
