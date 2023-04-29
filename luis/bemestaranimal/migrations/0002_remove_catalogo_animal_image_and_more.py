# Generated by Django 4.1.6 on 2023-02-10 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bemestaranimal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogo',
            name='animal_image',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='castrado',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='sexo',
        ),
        migrations.AddField(
            model_name='animal',
            name='idade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bemestaranimal.animal'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_tutor/', verbose_name='Foto do animal'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bemestaranimal.tutor'),
        ),
        migrations.CreateModel(
            name='Adotados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bemestaranimal.catalogo')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bemestaranimal.tutor')),
            ],
        ),
    ]
