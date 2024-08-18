from django.shortcuts import render
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.
def home(request):
    # subject ="Test_Mail from Django Server"
    # message ="this is a Demo-test mail"
    # from_email ="matemanu725@gmail.com"
    # recipient_list =["matemanu725@gmail.com"]
    # send_mail(subject,message,from_email,recipient_list)



    # ==============mass mail....................
    message1 = (
    "this is django-server-->1",
    "test-match-->1",
    "matemanu725@gmail.com",
    ["matemanu725@gmail.com", "himanshimete9@gmail.com"],
    )
    message2 = (
    "this is django-server-->2",
    "test-match--->2",
    "matemanu725@gmail.com",
    ["himanshimate9@gmail.com"],
    )
    message3 = (
    "this is django-server-->3",
    "test-match--->3",
    "matemanu725@gmail.com",
    ["himanshimete9@gmail.com"],
    )
    
    send_mass_mail((message1, message2, message3), fail_silently=False)
    
    return HttpResponse("done")
    