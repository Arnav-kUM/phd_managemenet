from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('students', views.AllStudents_Requests, name="all students data"),
    path('students/new', views.AddStudents_Request, name="add new students to database"),
    path('students/csv/new/', views.AddStudents_Request_csv, name="add new students to database"),
    path('students/<str:pk>', views.StudentbyID_Requests, name="single student data"),
    path('students/<str:pk>/logbook', views.Logbook_Requests, name="logbook of a student"),
    path('students/log/<str:pk>', views.Log_Requests, name="single log"),
    path('students/fields/<str:table_name>/<str:column_name>', views.Value_Requests, name="get distinct values in a Field in database"),
    path('students/columns/<str:table_name>', views.Field_Requests, name="get all Field in a database table"),
]