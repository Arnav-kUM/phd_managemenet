# Generated by Django 4.1.7 on 2023-04-06 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Designation', models.CharField(choices=[('Professor', 'Professor'), ('Dr.', 'Dr.')], max_length=255)),
                ('Department', models.CharField(blank=True, max_length=255, null=True)),
                ('College', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('Department', models.CharField(max_length=255)),
                ('Date_of_joining', models.DateField()),
                ('Batch', models.CharField(max_length=255)),
                ('Educational_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('Region', models.CharField(blank=True, max_length=255, null=True)),
                ('Admission_through', models.CharField(blank=True, max_length=255, null=True)),
                ('Source_of_funding', models.CharField(blank=True, max_length=255, null=True)),
                ('Project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Email_id', models.EmailField(max_length=255)),
                ('Student_status', models.CharField(choices=[('Terminated', 'Terminated'), ('Completed', 'Completed'), ('Shifted', 'Shifted')], max_length=255)),
                ('Year_of_leaving', models.DateField(blank=True, null=True)),
                ('Comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Advisor_Type', models.CharField(choices=[('Advisor 1', 'Advisor 1'), ('Advisor 2', 'Advisor 2'), ('Co-Advisor 2', 'Co-Advisor 2')], max_length=255)),
                ('Instructor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.instructor')),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]
