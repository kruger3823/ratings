# Generated by Django 2.1.9 on 2022-11-06 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_auto_20221106_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments',
            field=models.TextField(verbose_name='CLEANLINESS'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments3',
            field=models.TextField(verbose_name='SECURITY'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments4',
            field=models.TextField(verbose_name='TRANSPARENCY'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments5',
            field=models.TextField(verbose_name='FEE'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments6',
            field=models.TextField(verbose_name='EXTRACURICULUMS'),
        ),
    ]
