# Generated by Django 4.1.7 on 2023-03-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0010_remove_attribution_fichier'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribution',
            name='fichier',
            field=models.FileField(default=True, upload_to='uploads/'),
        ),
    ]
