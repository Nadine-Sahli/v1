# Generated by Django 4.2 on 2023-04-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registre', '0006_remove_projet_comp'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='comp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='registre.composteur'),
        ),
    ]