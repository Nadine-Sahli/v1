# Generated by Django 4.2 on 2023-04-27 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_nodes_proj'),
        ('MQTT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='po',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='map.nodes'),
        ),
    ]
