# Generated by Django 4.1.7 on 2023-04-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_date_of_joining_student_joining_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]
