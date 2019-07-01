from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from friends.models import Person
from friends.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here
def index(request):
    pList=Person.objects.all()
    return render(request,'index.html',{'mylist':pList})
def details(request, x):
    p=Person.objects.get(id=x)
    return render(request, 'details.html', {'p':p})
def contact(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        name=request.POST.get('contact_name')
        em=request.POST.get('contact_email')
        msg=request.POST.get('content')
        subject='Hello'+name+"mail from pythonfriend.com"
        from_email=settings.EMAIL_HOST_USER
        user_email=em
        to_list=[user_email,from_email]
        send_mail(subject,msg,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contact.html', {'form':form})
def thankyou(request):
    res=HttpResponse()
    res.write('<h2>Thanks for contacting us.</h2>')
    res.write('<h2>We just sent you a mail to you. Please check it.</h2>')
    return res
        
