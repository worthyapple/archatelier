from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactFormSubmission, IndexFormSubmission
from django.db import models

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        phone = request.POST.get('phone', 'Not provided')
        email = request.POST.get('email', 'Not provided')
        
        # Save the data to the database
        IndexFormSubmission.objects.create(
            name=name,
            phone=phone,
            email=email
        )

        return HttpResponse(f"Thank you, {name}! We have received your details.")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        mobile = request.POST.get('mobile', 'Not provided')
        city = request.POST.get('city', 'Not provided')
        email = request.POST.get('email', 'Not provided')
        pincode = request.POST.get('pincode', 'Not provided')
        project_size = request.POST.get('project_size', 'Not provided')
        project_location = request.POST.get('project_location', 'Not provided')
        budget = request.POST.get('budget', 'Not provided')
        requirements = request.POST.get('requirements', 'Not provided')


        # Save the data to the database
        ContactFormSubmission.objects.create(
            name=name,
            mobile=mobile,
            city=city,
            email=email,
            pincode=pincode,
            project_size=project_size,
            project_location=project_location,
            budget=budget,
            requirements=requirements
        )

        
        return HttpResponse(f"Thank you, {name}! We have received your details.")
    return render(request, 'contact.html')
