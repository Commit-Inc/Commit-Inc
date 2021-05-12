from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, JsonResponse
# import os
from django.contrib.auth.decorators import login_required
from .models import Client, DropYourEmail
from django.contrib.auth.decorators import login_required, permission_required
import openpyxl
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from commit import keyconfig

# makemigrations and stuff later?


def home(request):
    if request.method == "POST":
        email = request.POST["email-enter"]
        drop_email = DropYourEmail(droppedEmail=email)
        drop_email.save()

        # sg = sendgrid.SendGridAPIClient(api_key=keyconfig.SENSENDGRID_API_KEY)
        # to_emails = email
        # from_email = Email(keyconfig.FROM_EMAIL)
        # subject = "Welcome right?"
        # html_content = "<strong>hey</strong>"
        # mail = Mail(from_email, to_emails, subject, html_content)
        # response = sg.send(mail)
        # print(response)

        return render(request, "main/home.html", {"email": email})
    else:
        return render(request, "main/home.html", {})
    return render(request, "main/home.html", {})


def work(request):
    return render(request, "main/work.html", {})


def process(request):
    return render(request, "main/process.html", {})


def about(request):
    return render(request, "main/about.html", {})


def contact(request):
    if request.method == "POST":
        fName = request.POST["fName"]
        lName = request.POST["lName"]
        email = request.POST["email"]
        phone = request.POST["email"]
        company = request.POST["company"]
        extra = request.POST["extra"]
        requirements = request.POST["requirements"]
        client = Client(
            fName=fName,
            lName=lName,
            email=email,
            phone=phone,
            company=company,
            message=extra,
            requirements = requirements
        )
        client.save()

        # sg = sendgrid.SendGridAPIClient(api_key=keyconfig.SENSENDGRID_API_KEY)
        # to_emails = email
        # from_email = Email(keyconfig.FROM_EMAIL)
        # subject = "Welcome right?" 
        # html_content = "<strong>hey</strong>" 
        # mail = Mail(from_email, to_emails, subject, html_content)
        # response = sg.send(mail)
        # print(response)

        return render(request, "main/contact.html", {})
    else:
        return render(request, "main/contact.html", {})
    return render(request, "main/contact.html", {})


@permission_required("GET") #or @permission_required("admin.can_add_log_entry")
def getData(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="profile_data.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Potential Client Data"

    clients = Client.objects.all()
    row_data = [
        [
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Company",
            "Message",
        ]
    ]
    for client in clients:
        row = [
            client.fName,
            client.lName,
            client.email,
            client.email,
            client.phone,
            client.company,
            client.message,
        ]
        row_data.append(row)

    for line in row_data:
        ws.append(line)

    wb.save(response)
    return response
 

 #if the above mail client does not work, use
#  def send_email(html_message, subject, to_email):
#     from_email = Email('"Commit" <commit.net.in@gmail.com>')
#     content = Content("text/html", html_message)
#     mail = Mail(from_email, subject, to_email, content)
#     sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
#     response = sg.client.mail.send.post(request_body=mail.get())
#     _print("SendGrid mail")

# where html_message = html message?