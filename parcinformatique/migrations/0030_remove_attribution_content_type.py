# Generated by Django 4.1.7 on 2023-04-11 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcinformatique', '0029_attribution_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribution',
            name='content_type',
        ),
    ]