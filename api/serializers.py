from rest_framework.serializers import ModelSerializer
from .models import Student, Instructor, Advisor, Logbook

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class AdvisorSerializer(ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class LogbookSerializer(ModelSerializer):
    class Meta:
        model = Logbook
        fields = '__all__'