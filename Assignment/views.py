import json
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from .forms import userdata, loginform


# Create your views here.
def index(request):  # Function to Register a user
    form = userdata()
    if request.method == "POST":
        form = userdata(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            mail = request.POST.get('mail')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            print(mail)
            with open('Assignment/database.json', 'r') as f:
                if os.path.getsize('Assignment/database.json') == 0:  # To check if size is zero. Initial
                    userid = 1
                    data = {

                    }
                else:
                    data = json.load(f)
                    userid = len(data) + 1
                user_data = {
                    "userid": userid,
                    "username": username,
                    "mail": mail,
                    "password": password,
                    "mobile": mobile,
                    "address": address
                }
                data[userid] = user_data
                f.close()
                with open('Assignment/database.json', 'w') as f:
                    json.dump(data, f)
                    f.close()
                subject = "Your acccount Has been created."
                message = f"Hello {username}, Your account has been created with UserID: {userid} and password {password}"
                from_mail = "thrinadh.manubothu@gmail.com"
                recipient_list = [mail]
                send_mail(subject, message, from_mail, recipient_list, fail_silently=False)
                return render(request, 'created.html', {'data': userid})
    return render(request, 'index.html',{'form':form})


def logindata(request):  # Function to Handle Login Infomration
    forms = loginform
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        with open('Assignment/database.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if (data[i]['username'] == username and data[i]['password'] == password):
                    return render(request, 'loggedin.html', {'username': username, 'id': i})
            else:
                msg = "No Such User Found.Please Check the Credentials You Entered."
                return render(request, 'loggedin.html', {'msg': msg})
    return render(request, 'log.html', {'form': forms})


def userview(request):  # Function to view all the users data in JSON Fomat
    with open('Assignment/database.json', 'r') as f:
        if os.path.getsize('Assignment/database.json') == 0:
            return HttpResponse("No Users Registered. Register and then come here")
        else:
            data = json.load(f)
            return JsonResponse(data)
