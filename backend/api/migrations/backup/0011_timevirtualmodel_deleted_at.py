# Generated by Django 3.0.3 on 2020-06-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200612_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='timevirtualmodel',
            name='deleted_at',
            field=models.DateField(blank=True, null=True, verbose_name='Date de suppression'),
        ),
    ]
