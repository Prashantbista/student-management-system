"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView)
from django.contrib import admin
from django.urls import path, include
from students.views import ai_chat,home,list_students,get_course,add_coursedata,add_student,view_student,list_Course,add_course,list_subject,add_subject,delete_student,delete_course,edit_student 
from aboutus.views import about
from accounts.views import register,profile


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("students.urls_api")),
    path("", home, name="home"),
    path("about/", about,name="about"),
    path("students/",list_students,name="students"),
    path("students/add/",add_student,name="add_student"),
    path("students/<int:student_id>/",view_student,name="view_student"),
    path("course/", list_Course, name="list_Course"),
    path("add course/",add_course,name="add_course"),
    path("subject/",list_subject,name="list_subject"),
    path("add subject/",add_subject,name="add_subject"),
    path("students/delete/<int:student_id>/",delete_student, name="delete_student"),
    path("course/delete/<int:student_id>/",delete_course, name="delete_course"),
    path("students/edit/<int:student_id>/",edit_student,name="edit_student"),


    path("register/", register, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view (template_name="accounts/login.html"),name="login"),
    path("accounts/profile/",profile, name="profile"),
    path("accounts/logout/",auth_views.LogoutView.as_view(next_page="home"),name="logout"),
    path("course/get/<int:course_id>/",get_course,name="get_course"),
    path("course-data/add/",add_coursedata,name="add_course-data"),
    path("api/schema/",SpectacularAPIView.as_view(),name="schema",),
    path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),
    path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
    path("ai-chat/", ai_chat, name="ai_chat"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)