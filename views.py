from django.shortcuts import render
from .models import InternshipRegistration, Contact


def home(request):
    return render(request, 'home.html')


def register(request):
    message = ""

    if request.method == "POST":
        InternshipRegistration.objects.create(
            full_name=request.POST.get('full_name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            aadhaar_number=request.POST.get('aadhaar_number'),
            state=request.POST.get('state'),
            university_name=request.POST.get('university_name'),
            college_name=request.POST.get('college_name'),
            course=request.POST.get('course'),
            branch=request.POST.get('branch'),
            internship_type=request.POST.get('internship_type')
        )

        message = "Registration Successful"

    return render(request, 'register.html', {'message': message})


def courses(request):
    return render(request, 'courses.html')


def events(request):
    return render(request, 'event.html')


def contact(request):
    message = ""

    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        message = "Message Sent Successfully"

    return render(request, 'contact.html', {'message': message})


def about(request):
    return render(request, 'about.html')