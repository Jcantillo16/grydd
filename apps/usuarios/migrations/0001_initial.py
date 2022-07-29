# Generated by Django 4.0.6 on 2022-07-29 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'grydd_role',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('indicativo_telefono', models.CharField(blank=True, default='+57', max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='empresas.empresa')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.role')),
            ],
            options={
                'db_table': 'grydd_usuario',
            },
        ),
    ]
