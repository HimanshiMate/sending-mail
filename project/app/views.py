from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    subject ="Test_Mail from Django Server"
    message ="this is a Demo-test mail"
    from_email ="matemanu725@gmail.com"
    recipient_list =["matemanu725@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)
    
    return HttpResponse("done")
    