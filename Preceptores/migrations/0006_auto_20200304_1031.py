# Generated by Django 3.0.2 on 2020-03-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preceptores', '0005_auto_20200304_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduacao',
            name='g_ano_termino',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='graduacao',
            name='g_curso',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='graduacao',
            name='g_instituicao',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
