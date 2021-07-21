# Generated by Django 2.2.24 on 2021-07-21 14:33

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0078_add_external_builds_privacy_level_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTTPHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=256)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='http_headers', to='projects.Domain')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
