from django.urls import path
# from .api_views import StudentListCreateAPIView, StudentDetailAPIView
from .api_views import CourseListAPIView
from .api_views import StudentViewSet
from rest_framework.routers import DefaultRouter


router= DefaultRouter()

router.register("students", StudentViewSet , basename="student")


urlpatterns=[
    # path("students/", StudentListCreateAPIView.as_view(),name="student-list"),
    path("course/", CourseListAPIView.as_view(),name="course_list")
    #  path("students/<int:pk>/",StudentDetailAPIView.as_view(),name="student-deatil"),
]

urlpatterns += router.urls