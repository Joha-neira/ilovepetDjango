# Generated by Django 2.2.6 on 2019-11-20 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fechaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('dueno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Cliente')),
            ],
        ),
    ]
