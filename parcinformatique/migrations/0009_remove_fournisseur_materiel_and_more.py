# Generated by Django 4.1.7 on 2023-03-23 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0008_attribution_fichier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='materiel',
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='domaine_activite',
            field=models.CharField(blank=True, default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='situation_geographique',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='maintenancier',
            name='domaine_activite',
            field=models.CharField(blank=True, default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='maintenancier',
            name='situation_geographique',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='materiel',
            name='fournisseur',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='parcinformatique.fournisseur'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='garantie',
            field=models.PositiveIntegerField(),
        ),
    ]
