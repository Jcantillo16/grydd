# Generated by Django 4.0.6 on 2022-07-29 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('punto_de_acceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horario', to='empresas.puntosdeacceso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horario', to='usuarios.usuario')),
            ],
            options={
                'db_table': 'grydd_horario',
            },
        ),
    ]
