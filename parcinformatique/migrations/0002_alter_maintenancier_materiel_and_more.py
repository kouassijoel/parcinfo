# Generated by Django 4.1.7 on 2023-03-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancier',
            name='materiel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcinformatique.materiel'),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='type_materiel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcinformatique.typemateriel'),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='lieu_naissance',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='numero_pieces',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='type_pieces',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcinformatique.typepieces'),
        ),
        migrations.AlterField(
            model_name='typemateriel',
            name='libelle',
            field=models.CharField(choices=[('PC', 'PC'), ('DISQUE DUR', 'DISQUE DUR'), ('IMPRIM', 'IMPRIM')], max_length=50),
        ),
    ]
