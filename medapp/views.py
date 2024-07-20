from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import  HttpResponse,render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.utils import translation
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import json 

def home(request):
    blogs = Blog.objects.all()[0:4]
    services = Service.objects.all()[0:4]
    doctors = Doctor.objects.all()[0:4]
    slider = HomeSlider.objects.filter(in_home=True)
    context = {
        'doctors':doctors,
        'services':services,
        'blogs':blogs,
        'slider':slider
    }

    return render(request,'index.html',context)

def about(request):
    context = {
    }
    return render(request,'about-us.html',context)

def contact(request):
    context = {
    }
    return render(request,'contact-us.html',context)

def services(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'services.html',context)


#DetailViews

def service(request,slug):
    service = get_object_or_404(Service,slug=slug)
    services = Service.objects.all()
    context = {
        'service':service,
        'services':services
    }
    return render(request,'service-details.html',context)

#Json
def message(request):
    if request.method == 'POST':
        newmessage = Messageform(request.POST)
        if newmessage.is_valid():
            newmessage.save()
            data = {'status': 'success','message': 'Məktubunuz uğurla göndərildi!'}
            return JsonResponse(data)
        else:
            print(newmessage.errors)
            return JsonResponse({'status': 'error', 'message': 'Form hataları var!', 'errors': newmessage.errors})
        
    else:
        return HttpResponse(status=405) 

def d_message(request):
    if request.method == 'POST':
        newmessage = DoctorMessageform(request.POST)
        if newmessage.is_valid():
            newmessage.save()
            data = {'status': 'success','message': 'Məktubunuz uğurla göndərildi!'}
            return JsonResponse(data)
        else:
            print(newmessage.errors)
            return JsonResponse({'status': 'error', 'message': 'Form hataları var!', 'errors': newmessage.errors})
        
    else:
        return HttpResponse(status=405) 


def comment(request):
    if request.method == 'POST':
        newmessage = CommentForm(request.POST)
        if newmessage.is_valid():
            newmessage.save()
            data = {'status': 'success','message': 'Şərhiniz uğurla göndərildi!'}
            return JsonResponse(data)
        else:
            print(newmessage.errors)
            return JsonResponse({'status': 'error', 'message': 'Xəta var!', 'errors': newmessage.errors})
        
    else:
        return HttpResponse(status=405) 

def blogs(request):
    blogs = Blog.objects.all()
    related_blogs = Blog.objects.all()[::-1][0:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    category = request.GET.get('category')
    form = SearchForm(request.GET or None)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    if category:
        blogs = Blog.objects.filter(category__slug = category)
        currentCategory = Category.objects.get(slug = category)
    else:
        currentCategory = ''

    context = {
        'blogs':blogs,
        'categories':categories,
        'tags':tags,
        'form':form,
        'currentCategory':currentCategory,
        'related_blogs':related_blogs
    }
    return render(request,'blog-classic.html',context)

def blog(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    related_blogs = Blog.objects.exclude(slug=blog.slug)[::-1][0:3]
    categories = Category.objects.all()
    form = SearchForm(request.GET or None)
    context = {
        'blog':blog,
        'categories':categories,
        'form':form,
        'related_blogs':related_blogs
    }
    return render(request,'blog-details.html',context)

def team(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors':doctors
    }

    return render(request,'doctors.html',context)

def doctor(request,slug):
    doctor = get_object_or_404(Doctor,slug=slug)
    
    context = {
        'doctor':doctor
    }

    return render(request,'doctor.html',context)