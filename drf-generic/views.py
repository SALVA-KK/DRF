from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Student
from .serializers import StudentSerializer


class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()

        
        age = self.request.query_params.get('age')
        if age:
            queryset = queryset.filter(age=age)

        order = self.request.query_params.get('ordering')
        if order == 'name':
            queryset = queryset.order_by('name')
        elif order == '-name':
            queryset = queryset.order_by('-name')

        return queryset

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer