# Generated by Django 3.0.7 on 2020-08-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0005_doctor_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default=('correo', '@gmail.com'), max_length=25),
            preserve_default=False,
        ),
    ]
