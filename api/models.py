from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    Id = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Email_Id = models.EmailField(max_length=255, unique=True)
    Contingency_points = models.PositiveIntegerField(default=0)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    Department = models.CharField(max_length=255, choices=[('CSE', 'CSE'), ('CB', 'CB'), ('ECE', 'ECE'), ('HCD', 'HCD'), ('SSH', 'SSH'), ('Maths', 'Maths')])
    Joining_date = models.DateField()
    Batch = models.CharField(max_length=255)
    Educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    Region = models.CharField(max_length=255, null=True, blank=True)
    Admission_through = models.CharField(max_length=255, null=True, blank=True)
    Source_of_funding = models.CharField(max_length=255, null=True, blank=True)
    Project_name = models.CharField(max_length=255, null=True, blank=True)
    Student_status = models.CharField(max_length=255, choices=[('Terminated', 'Terminated'), ('Completed', 'Completed'), ('Shifted', 'Shifted'), ('Semester Leave', 'Semester Leave'), ('Active', 'Active')])
    Year_of_leaving = models.PositiveIntegerField(validators=[
                MinValueValidator(2000), 
                MaxValueValidator(datetime.date.today().year+10)], help_text="Use the following format: <YYYY>",null=True, blank=True)
    Comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Id
    

class Instructor(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255, choices=[('Professor', 'Professor'), ('Dr.', 'Dr.')])
    Department = models.CharField(max_length=255, choices=[('CSE', 'CSE'), ('CB', 'CB'), ('ECE', 'ECE'), ('HCD', 'HCD'), ('SSH', 'SSH'), ('Maths', 'Maths')])
    College = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.Id)
    
class Advisor(models.Model):
    Instructor_Id = models.ForeignKey(Instructor, null=True, blank=True, on_delete=models.SET_NULL)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Advisor_Type = models.CharField(max_length=255, choices=[('Advisor 1', 'Advisor 1'), ('Advisor 2', 'Advisor 2'), ('Co-Advisor 2', 'Co-Advisor 2')])


class Logbook(models.Model):
    Log_Id = models.AutoField(primary_key=True)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Item = models.TextField()
    Quantity = models.PositiveIntegerField(default=1)
    Price = models.PositiveIntegerField()
    Source = models.CharField(max_length=255, null=True, blank=True)
    Credit = models.TextField(null=True, blank=True)
    Claim_amount = models.PositiveIntegerField()
    Opening_balance = models.PositiveIntegerField()
    Opening_balance_on_date = models.DateField()
    Closing_balance = models.PositiveIntegerField()
    Closing_balance_on_date = models.DateField()
    Forward_by = models.CharField(max_length=255)
    Forwarded_on_date = models.DateField()
    Sanctioned_amount = models.PositiveIntegerField()
    Remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.Log_Id)