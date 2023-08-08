from rest_framework.response import Response
from django.apps import apps
from .models import Student, Instructor, Advisor, Logbook
from .serializers import StudentSerializer, InstructorSerializer, AdvisorSerializer, LogbookSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
import csv
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Student
import json

def getStudentbyID(request, pk):
    student = Student.objects.get(Id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

def editStudentByID(request, pk):
    data = request.data
    student = Student.objects.get(Id=pk)
    print(data)
    # print(student)
    serializer = StudentSerializer(instance=student, data=data)
    if serializer.is_valid():
        serializer.save()
    else: print(serializer.errors)
    return Response(serializer.data)

# from rest_framework import status

def addStudents(request):
    serializer = StudentSerializer(data=request.data, many=True)
    print(request.data)
    if serializer.is_valid():
        students_data = serializer.validated_data
        for student_data in students_data:
            student = Student.objects.create(**student_data)
        return Response(serializer.data, status=201)
    else:
        error_dict = {}
        if isinstance(serializer.errors, list):
            for error in serializer.errors:
                for key, value in error.items():
                    if key == "non_field_errors":
                        error_dict[key] = value[0]
                    else:
                        error_dict[key] = value[0]
        else:
            for key, value in serializer.errors.items():
                if key == "non_field_errors":
                    error_dict[key] = value[0]
                else:
                    error_dict[key] = value[0]
        print(error_dict)            
        return Response(error_dict, status=400)


from django.http import HttpResponse
    
def add_students_from_csv(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_contents = uploaded_file.read()
        data_str = file_contents.decode('utf-8')
        raw_data = json.loads(data_str)
       
        order_data = []
        for i in range(1,len(raw_data)):
            dict = {}
            for j in range(0,len(raw_data[0])):
                if raw_data[i][j] != "Null":
                    dict[raw_data[0][j]] = raw_data[i][j]
                    
            order_data.append(dict)
        print(len(order_data[0])," ",len(order_data))
        serializer = StudentSerializer(data=order_data,many=True)
        if serializer.is_valid():
            students_data = serializer.validated_data
            for i in students_data:
                student = Student.objects.create(**i)
            print("valid")
        else:
            print("Invalid")
            return Response("Invalid")
        return HttpResponse("hi")
    else:
        return HttpResponse("Invalid request method")

def getStudents(request):
    filter = request.data
    filtered_students = Student.objects.all()
    search = request.query_params.get('search')

    if filter:
        if 'Gender' in filter:
            value = filter['Gender']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Gender__in=value)
            else:
                filtered_students = filtered_students.filter(Gender=value)
        if 'Department' in filter:
            value = filter['Department']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Department__in=value)
            else:
                filtered_students = filtered_students.filter(Department=value)
        if 'Region' in filter:
            value = filter['Region']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Region__in=value)
            else:
                filtered_students = filtered_students.filter(Region=value)
        if 'Student status' in filter:
            value = filter['Student status']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Student_status__in=value)
            else:
                filtered_students = filtered_students.filter(Student_status=value)
        if 'Source of funding' in filter:
            value = filter['Source of funding']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Source_of_funding__in=value)
            else:
                filtered_students = filtered_students.filter(Source_of_funding=value)
        if 'Batch' in filter:
            value = filter['Batch']
            if isinstance(value, list):
                filtered_students = filtered_students.filter(Batch__in=value)
            else:
                filtered_students = filtered_students.filter(Batch=value)

    if search is not None and len(search) > 0:
        if ('@' in search): filtered_students = filtered_students.filter(Email_Id__icontains=search)
        elif (search.isalpha()): filtered_students = filtered_students.filter(Name__icontains=search)
        else: filtered_students = filtered_students.filter(Id__icontains=search)

    serializer = StudentSerializer(filtered_students, many=True)
    return Response(serializer.data)




def getLog(request, pk):
    logs = Logbook.objects.filter(Student_Id=pk)
    serializer = LogbookSerializer(logs, many=True)
    return Response(serializer.data)

def editLog(request, pk):
    data = request.data
    log = Logbook.objects.get(Log_Id=pk)
    serializer = LogbookSerializer(instance=log, data=data)
    if serializer.is_valid():
        serializer.save()
    else: print(serializer.errors)
    return Response(serializer.data)

def deleteLog(request, pk):
    log = Logbook.objects.get(Log_Id=pk)
    log.delete()
    return Response('Log was deleted!')

def newLog(request, pk):    
    data = request.data
    student = Student.objects.get(Id=pk)
    log = Logbook.objects.create(
        Student_Id = student,
        **data
    )
    serializer = LogbookSerializer(log, many=False)
    return Response(serializer.data)

def get_distinct_values(request, table_name, column_name):
    # Get the model class corresponding to the table_name
    model_class = apps.get_model(app_label='api', model_name=table_name)

    # Get the distinct values in the specified column
    values = model_class.objects.values_list(column_name, flat=True).distinct()

    # Return the distinct values as a response
    return Response(list(values))

def get_table_fields(request, table_name):
    # Get the model class corresponding to the table_name
    model_class = apps.get_model(app_label='api', model_name=table_name)

    # Get the field names of the model class
    field_names = [field.name for field in model_class._meta.fields]

    # Return the field names as a JSON response
    return Response(field_names)