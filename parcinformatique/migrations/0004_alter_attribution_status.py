# Generated by Django 4.1.7 on 2023-03-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0003_ressource_date_naissances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribution',
            name='status',
            field=models.CharField(choices=[('ATTRIBUER', 'ATTRIBUER'), ('NON ATTRIBUER', 'NON ATTRIBUER')], default=True, max_length=50),
        ),
    ]
