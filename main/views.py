
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Client, DropYourEmail
from django.contrib.auth.decorators import login_required, permission_required
import openpyxl
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from commit import keyconfig


def home(request):
    if request.method == "POST":
        email = request.POST["email-enter"]
        drop_email = DropYourEmail(droppedEmail=email)
        drop_email.save()

        if email:
            message = Mail(
                from_email='commit.net.in@gmail.com',
                to_emails=str(email),
                subject='TEsting mail',
                html_content= render_to_string("main/email.html"))
            try:
                sg = SendGridAPIClient(api_key=keyconfig.SENSENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
        else:
            return redirect('home')                
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
        if email:
            message = Mail(
                from_email='commit.net.in@gmail.com',
                to_emails=str(email),
                subject='TEsting mail',
                html_content='<strong>hey</strong>')
            try:
                sg = SendGridAPIClient(api_key=keyconfig.SENSENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
        else:
            return redirect('home')           
        return render(request, "main/contact.html", {})
    else:
        return render(request, "main/contact.html", {})
    return render(request, "main/contact.html", {})


@permission_required("GET")
def getData(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="ClientData.xlsx"'

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
            "Requirements"
        ]
    ]
    for client in clients:
        row = [
            client.fName,
            client.lName,
            client.email,
            client.phone,
            client.company,
            client.message,
            client.requirements
        ]
        row_data.append(row)

    for line in row_data:
        ws.append(line)

    wb.save(response)
    return response
 