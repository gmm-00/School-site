# Generated by Django 4.2.4 on 2023-08-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilottama', '0018_alter_result_student_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
