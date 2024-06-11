# Generated by Django 5.0.6 on 2024-06-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskid', models.AutoField(db_column='TaskID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('assignto', models.CharField(blank=True, db_column='AssignTo', max_length=40, null=True)),
                ('startdate', models.DateField(blank=True, db_column='startDate', null=True)),
                ('duedate', models.DateField(blank=True, db_column='dueDate', null=True)),
                ('status', models.CharField(blank=True, max_length=9, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=1000, null=True)),
            ],
        ),
    ]