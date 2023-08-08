from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import utils


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/student_database',
            'method': 'GET',
            'body': None,
            'description': 'Returns all student database'
        },
        {
            'Endpoint': '/student/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single student data'
        },
        {
            'Endpoint': '/student/add_new/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Adds a new Student data to the database'
        },
        {
            'Endpoint': '/student/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update a student\'s information in the database'
        },
    ]
    return Response(routes)

@api_view(['GET', 'PUT'])
def StudentbyID_Requests(request, pk):
    if request.method == 'GET':
        return utils.getStudentbyID(request, pk)
    
    if request.method == 'PUT':
        return utils.editStudentByID(request, pk)

@api_view(['POST'])
def AllStudents_Requests(request):
    return utils.getStudents(request)
   
@api_view(['POST'])
def AddStudents_Request(request):
    return utils.addStudents(request)

@api_view(['POST'])
def AddStudents_Request_csv(request):
    return utils.add_students_from_csv(request)
    
@api_view(['GET', 'POST'])
def Logbook_Requests(request, pk):
    if request.method == 'GET':
        return utils.getLog(request, pk)
    
    if request.method == 'POST':
        return utils.newLog(request, pk)
   
@api_view(['PUT', 'DELETE'])
def Log_Requests(request, pk):
    if request.method == 'PUT':
        return utils.editLog(request, pk)
    
    if request.method == 'DELETE':
        return utils.deleteLog(request, pk)
    
@api_view(['GET'])
def Value_Requests(request, table_name, column_name):
    return utils.get_distinct_values(request, table_name, column_name)

@api_view(['GET'])
def Field_Requests(request, table_name):
    return utils.get_table_fields(request, table_name)