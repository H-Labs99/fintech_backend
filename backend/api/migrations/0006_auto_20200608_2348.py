# Generated by Django 3.0.3 on 2020-06-08 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200608_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='addresse',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
