# Generated by Django 2.1.7 on 2019-05-16 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0002_auto_20190516_0524'),
        ('Log_In', '0002_auto_20190516_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=100)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Announcements', to='Courses.Courses')),
                ('Lect_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log_In.Lecturer')),
            ],
        ),
    ]
