# Generated by Django 5.0.4 on 2024-04-12 21:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='symptom',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symptoms.medicalcondition')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symptoms.section')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symptoms.symptom')),
            ],
        ),
    ]