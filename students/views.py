from django.shortcuts import render,redirect
from.models import Student
from.models import Course
from.models import AIConversation, Subject
from.ai_servies import  ask_ai
from .forms import  StudentForm
import json


# Create your views here.
from django.http import HttpResponse, JsonResponse


def ai_chat (request):
    answer=""
    error=""
    question=""

    if request.method == "POST":
        question = request.POST.get("question","").strip()
        if question:
            try:
                answer= ask_ai(question)
                AIConversation.objects.create(question=question,answer=answer)
            except Exception:
                error = "Sorry, the AI service is unavailable"

    converations=AIConversation.objects.order_by("-created_at")
    context = {
        'titile':'Ai chat Program',
        'header':'Ai chat Asssitent',
        'answer':answer,
        'error':error,
        'question':question,
        'converstions':converations
    }
    return render(request,"students/ai_chat.html",context)





def add_coursedata(requset):
    if requset.method == "POST":
        requset_data = json.loads(requset.body)
        course = Course.objects.create(name=requset_data ["name"])

        data={
            "id":course.id,
            "name": course.name
        }
        return JsonResponse(data, status=200)

def get_course(request, course_id):
    try:
        course=Course.objects.get(id=course_id)
        data={
        "id": course.id,
        "name": course.name
    }
        return JsonResponse(data, status=200)
    except Course.DoesNotExist:
        return JsonResponse({"error":f"Course with course id {course_id} Does not exist."},stattus=404)

def home(request):
    # return HttpResponse ("hello Django!")
    context={
        'titile':'student management',
        'header':'welcome',
    }
    return render(request,"students/home.html",context)


def list_students(request):
    students=Student.objects.all()
    context={
        "students":students,
        "header":"student_list",
        "title":"Student",
    }
    return render(request,"students/list_student.html",context)


def view_student(request,student_id):
    student = Student.objects.get(id=student_id)
    subjects= student.subjects.all()
    context={
        'header':'Student detail',
        'title':'student detail',
        'student':student,
        'subjects':subjects,
    }
    return render (request, "students/view_student.html",context)

def list_Course(request):
    course= Course.objects.all()
    context={
        "header":"courses",
        "paragraph":"this is a list of course",
        'course':course,
    }
    return render(request, "students/list course.html", context)


def add_course(request):
    if request.method == "POST":
        course=request.POST.get("course")
        Course.objects.create(name=course)
        return redirect("list_Course")
    else:
        context={
            "header":"course form",
        }

        return render(request,"students/add_course.html",context)

    
def list_subject(request):
    subject=Subject.objects.all()
    context={
            "header":"Subjects",
            "paragraph":"this is a list of subject",
            'subject':subject,
        }
    return render(request,"students/list_subject.html",context)

def add_subject(request):
    if request.method == "POST":
        subject=request.POST.get("subject")
        Subject.objects.create(name=subject)
        return redirect ("list_subject")
    else:
        context={
            "header":"ADD SUBJECT",
    }
    return render (request,"students/add_subject.html",context)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    context= {
        "header":"Add student",
        'title':'add student',
        'form':form
    }
    return render(request,"students/add_student.html",context)

# def add_student(request):
#     if request.method == "POST":
#         name= request.POST.get("name")
#         email= request.POST.get("email")
#         age= request.POST.get("age")
#         address= request.POST.get("address")
#         course_id=request.POST.get("course_id")

#         Student.objects.create(name=name, email=email, age=age, address=address, course_id=course_id)
#         return redirect('students')
#     else:
#         courses=Course.objects.all()
#         context= {
#             "header":"FORM",
#             "courses":courses,
#         }
#         return render(request,"students/add_student.html",context)

def delete_student(request, student_id):
    student=Student.objects.get(id=student_id)
    student.delete()
    return redirect ('students')

def delete_course(request, student_id):
    course=Course.objects.get(id=student_id)
    course.delete()
    return redirect ('list_Course')



def edit_student(request, student_id):
    student=Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    context= {
        "header":"Add student",
        'title':'add student',
        'form':form
    }
    return render(request,"students/add_student.html",context)