import json
from django.shortcuts import render, redirect,HttpResponse
import pandas as pd
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages  #
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, "home.html")


def features(request):
    return render(request, "features.html")


def use_cases_strategy(request):
    return render(request, "use_cases_strategy.html")


def use_cases_invester(request):
    return render(request, "use_cases_invester.html")


def Strategy_builder_straddle(request):
    return render(request, "Strategy_builder_straddle.html")


def dashboard(request):
    return render(request, "dashboard.html")


def help_support(request):
    return render(request, "help_support.html")


def learning_center(request):
    return render(request, "learning_center.html")


def blog(request):
    return render(request, "blog.html")


def reset_password(request):
    return render(request, "reset_password.html")


def Symbol_filter(request):
    if request.method == "POST":
        symbol = request.POST['symbols']
        expiry_dates = request.POST["expiryDates"]
        print(symbol, expiry_dates)

        url = 'https://www.nseindia.com/api/option-chain-indices?symbol='+symbol
        print(url)
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        session = requests.Session()

        data = session.get(url, headers=headers).json()["records"]["data"]
        ocdata = []

        for i in data:
            for j, k in i.items():
                if j == "CE" or j == "PE":
                    info = k
                    info['instrumentType'] = j
                    ocdata.append(info)
        dataopt = pd.DataFrame(ocdata)
        filtered_data = dataopt[dataopt['expiryDate'] == str(expiry_dates)]
        if not filtered_data.empty:
            print(filtered_data)
            filtered_datas = filtered_data.head(100)
            print(filtered_datas)
            json_records = filtered_datas.reset_index().to_json(orient='records')
            data_filter = []
            data_filter = json.loads(json_records)

        else:
            print("No data available for the specified expiry date.")
        return render(request, 'Symbol_filter.html', {"dataframe": data_filter})

    else:
        url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        print(url)
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        session = requests.Session()

        data = session.get(url, headers=headers).json()["records"]["data"]
        ocdata = []

        for i in data:
            for j, k in i.items():
                if j == "CE" or j == "PE":
                    info = k
                    info['instrumentType'] = j
                    ocdata.append(info)
        dataopt = pd.DataFrame(ocdata)
        datashort = dataopt.head(100)
        json_records = datashort.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
    return render(request, "Symbol_filter.html", {"dataframe": data})


def signUp(request):
    if request.method == "POST":
        fname = request.POST["name"]
        email = request.POST["email"]
        phone_code = request.POST["phone_code"]
        mobile = request.POST["mobile"]
        country_id = request.POST.get("country_id","")
        state_id = request.POST.get("state_id","")
        password = request.POST["password"]
        Cofirm_password = request.POST["Cofirm_password"]
        if User.objects.filter(email=email):
                messages.warning(request, 'Email already being taken')
                return redirect('/')
        else:
          Mysignup = User.objects.create_user(
              full_name=fname,
              email=email,
              Mobile_number=mobile,
              password=password,
              confirm_password=Cofirm_password,
              Country=country_id,
              State=state_id,
              Phone_code=phone_code,
          )
          Mysignup.save()

          # Picture=Display_picture(image=images)
          # Picture.save()
          messages.success(
              request, 'You have successfully signed up , please login with correct credential')
          redirect('/')
    return render(request,'home.html')


def login_user(request):
    if request.method == 'POST':
        Email = request.POST['email']
        password = request.POST['password']
        print(Email, password)
        user = authenticate(email=Email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect("/")
        else:
            messages.error(request, 'Invalid credential')
            return redirect("/")


def logout_user(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect("/")