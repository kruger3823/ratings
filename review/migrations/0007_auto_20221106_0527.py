# Generated by Django 2.1.9 on 2022-11-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20221106_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='assignedTeacherId',
        ),
        migrations.AddField(
            model_name='review',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='assignedSubId',
            field=models.CharField(choices=[('1', 'Maths'), ('2', 'Chemistry'), ('3', 'Physics'), ('4', 'Biology'), ('4', 'Hindi')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]