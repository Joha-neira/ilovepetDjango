<<<<<<< HEAD
# Generated by Django 2.2.6 on 2019-11-16 00:15

from django.db import migrations, models
=======
# Generated by Django 2.2.6 on 2019-11-21 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> master
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('numeroTelefono', models.IntegerField()),
<<<<<<< HEAD
                ('correo', models.CharField(max_length=30)),
=======
>>>>>>> master
                ('fechaNacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=25)),
                ('comuna', models.CharField(max_length=30)),
                ('numeroContacto', models.IntegerField()),
                ('telefonoOficina', models.IntegerField()),
                ('profesion', models.CharField(max_length=20)),
<<<<<<< HEAD
=======
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('rutMascota', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('dueno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Cliente')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.TipoMascota')),
>>>>>>> master
            ],
        ),
    ]
