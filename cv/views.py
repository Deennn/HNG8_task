from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['full-name']
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        return HttpResponse("Thank you for reaching out, we will get back to you shortly....")
    else:
        return render(request, 'home.html', {})

