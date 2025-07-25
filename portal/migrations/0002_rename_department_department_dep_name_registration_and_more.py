# Generated by Django 5.1.6 on 2025-03-24 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='dep_name',
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('registeredfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courselist', to='portal.course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scgpa', models.FloatField()),
                ('cgpa', models.FloatField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentlist', to='portal.department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='assesment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.studentprofile'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
