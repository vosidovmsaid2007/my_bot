# Generated by Django 3.2.11 on 2024-01-18 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_test_text_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='level_m',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.levels'),
        ),
    ]
