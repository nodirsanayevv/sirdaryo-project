# Generated by Django 4.0.4 on 2022-05-17 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_period_period_id_practis_period_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='files')),
                ('practiceworker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.practis')),
            ],
        ),
    ]