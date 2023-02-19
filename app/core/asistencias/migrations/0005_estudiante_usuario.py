# Generated by Django 4.1.7 on 2023-02-19 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asistencias', '0004_remove_estudiante_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
