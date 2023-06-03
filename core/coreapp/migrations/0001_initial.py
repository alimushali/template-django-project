# Generated by Django 4.2.1 on 2023-06-03 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUnit1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('integer_property', models.IntegerField()),
            ],
            options={
                'db_table': 'coreapp_abstract_unit_1',
            },
        ),
        migrations.CreateModel(
            name='LinkedUnit1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('integer_property', models.IntegerField()),
                ('numeric_property', models.DecimalField(decimal_places=10, max_digits=19)),
                ('abstract_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.abstractunit1')),
            ],
            options={
                'db_table': 'coreapp_linked_unit_1',
            },
        ),
    ]
