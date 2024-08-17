from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.
def home(request):
    subject ="Test_Mail from Django Server"
    message ="this is a Demo-test mail"
    from_email ="matemanu725@gmail.com"
    recipient_list =["matemanu725@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)



    # ==============mass mail....................
    message1 = (
    "Subject here",
    "Here is the message",
    "from@example.com",
    ["first@example.com", "other@example.com"],
    )
    message2 = (
    "Another Subject",
    "Here is another message",
    "from@example.com",
    ["second@test.com"],
    )
    send_mass_mail((message1, message2), fail_silently=False)
    
    return HttpResponse("done")
    