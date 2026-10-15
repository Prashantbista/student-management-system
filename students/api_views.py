from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import generics
from rest_framework import viewsets
from .models import Student
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import StudentSerializer
from .serializers import CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        permission_classes= [IsAuthenticatedOrReadOnly]

        filter_backends = [
            DjangoFilterBackend,
            SearchFilter,
            OrderingFilter,
        ]

        filterset_fields = ["age", "course"]
        search_fields = ["name", "email", "address"]
        ordering_fields = ["name", "age"]
        ordering = ["id"]




# class StudentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer













# class StudentListAPIView(APIView):
#     def get(self, request):
#         students = Student.objects.all()

#         serializer= StudentSerializer(students, many=True)

#         return Response(serializer.data)

class CourseListAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        course = Course.objects.all()

        serializer= CourseSerializer(course, many=True)

        return Response(serializer.data)