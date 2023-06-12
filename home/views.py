from .models import Top_Gainer
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import JsonResponse
import uuid
import json
from django.shortcuts import render, redirect, HttpResponse
import pandas as pd
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages  #
from django.contrib.auth import get_user_model
from .models import ChartData
from home.helper import send_forget_password_mail
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


def Futures_Buildup(request):
    return render(request, "Futures_Buildup.html")


# def fetch_top_gainers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()

#     top_gainers = []
#     for stock in data['FOSec']['data']:
#         symbol = stock['symbol']
#         previous_close = stock['prev_price']
#         current_price = stock['ltp']

#         if symbol and previous_close and current_price:
#             gain_percentage = round(
#                 ((current_price - previous_close) / previous_close) * 100, 2)
#             top_gainers.append({
#                 "symbol": symbol,
#                 "gain_percentage": gain_percentage
#             })

#     top_gainers.sort(key=lambda x: x['gain_percentage'], reverse=True)
#     return top_gainers[:10]


# def fetch_top_losers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=loosers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()

#     top_losers = []
#     for stock in data['FOSec']['data']:
#         symbol_loser = stock['symbol']
#         previous_close = stock['prev_price']
#         current_price = stock['ltp']

#         if symbol_loser and previous_close and current_price:
#             loss_percentage = round(
#                 ((previous_close - current_price) / previous_close) * 100, 2)
#             top_losers.append({
#                 "symbol_loser": symbol_loser,
#                 "loss_percentage": loss_percentage
#             })

#     top_losers.sort(key=lambda x: x['loss_percentage'], reverse=True)
#     return top_losers[:10]


def fetch_top_gainers():
    url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except ValueError:
        data = None

    top_gainers = []
    if data and 'FOSec' in data and 'data' in data['FOSec']:
        for stock in data['FOSec']['data']:
            symbol = stock['symbol']
            previous_close = stock['prev_price']
            current_price = stock['ltp']

            if symbol and previous_close and current_price:
                gain_percentage = round(
                    ((current_price - previous_close) / previous_close) * 100, 2)
                top_gainers.append({
                    "symbol": symbol,
                    "gain_percentage": gain_percentage
                })

    top_gainers.sort(key=lambda x: x['gain_percentage'], reverse=True)
    return top_gainers[:10]

import requests
from django.shortcuts import render
from .models import Top_Loser

def fetch_top_losers():
    url = "https://www.nseindia.com/api/live-analysis-variations?index=loosers"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except ValueError:
        data = None

    top_losers = []
    if data and 'FOSec' in data and 'data' in data['FOSec']:
        for stock in data['FOSec']['data']:
            symbol = stock['symbol']
            previous_close = stock['prev_price']
            current_price = stock['ltp']

            if symbol and previous_close and current_price:
                loss_percentage = round(((previous_close - current_price) / previous_close) * 100, 2)
                loss_percentage_with_sign = f"-{loss_percentage}"
                top_losers.append({
                    "symbol": symbol,
                    "loss_percentage": loss_percentage_with_sign
                })

    top_losers.sort(key=lambda x: x['loss_percentage'], reverse=True)
    return top_losers[:10]





def chart_topgainer(request):

    try:
        top_losers = fetch_top_losers()
        symbols = [loser['symbol'] for loser in top_losers]
        loss_percentages = [loser['loss_percentage'] for loser in top_losers]

        # Replace existing data in the database with new data
        Top_Loser.objects.all().delete()  # Clear existing data
        Top_Loser.objects.create(top_losers=", ".join(symbols))

    except Exception as e:
        # Retrieve the data from the database
        top_loser_data = Top_Loser.objects.first()
        if top_loser_data:
            symbols = top_loser_data.top_losers.split(", ")
            loss_percentages = []
        else:
            symbols = []
            loss_percentages = []

    context = {
        'symbols': symbols,
        'loss_percentages': loss_percentages,
    }



    return render(request, 'chart_topgainer.html', context)


def dashboard(request):
    try:
        top_losers = fetch_top_losers()
        symbols = [loser['symbol'] for loser in top_losers]
        loss_percentages = [loser['loss_percentage'] for loser in top_losers]

        # Replace existing data in the database with new data
        Top_Loser.objects.all().delete()  # Clear existing data
        Top_Loser.objects.create(top_losers=", ".join(symbols))

    except Exception as e:
        # Retrieve the data from the database
        top_loser_data = Top_Loser.objects.first()
        if top_loser_data:
            symbols = top_loser_data.top_losers.split(", ")
            loss_percentages = []
        else:
            symbols = []
            loss_percentages = []

    context = {
        'symbols_losers': symbols,
        'loss_percentages': loss_percentages,
    }
    try:
        top_gainers = fetch_top_gainers()
        symbols = [gainer['symbol'] for gainer in top_gainers]
        gain_percentages = [gainer['gain_percentage']
                            for gainer in top_gainers]

        # Replace existing data in the database with new data
        Top_Gainer.objects.all().delete()  # Clear existing data
        Top_Gainer.objects.create(top_gainers=", ".join(symbols))

    except Exception as e:
        # Retrieve the data from the database
        top_gainer_data = Top_Gainer.objects.first()
        if top_gainer_data:
            symbols = top_gainer_data.top_gainers.split(", ")
            gain_percentages = []
        else:
            symbols = []
            gain_percentages = []

    context = {
        'symbols': symbols,
        'gain_percentages': gain_percentages,
    }

    url = "https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", str(e))
        data = None

    if data is not None:

        sorted_data = sorted(data['data'], key=lambda x: x['avgInOI'])

        top_symbols_lowest = sorted_data[:10]

        symbols_lowest = [symbol_data['symbol']
                          for symbol_data in top_symbols_lowest]
        avgInOI_values_lowest = [symbol_data['avgInOI']
                                 for symbol_data in top_symbols_lowest]

        sorted_data = sorted(
            data['data'], key=lambda x: x['avgInOI'], reverse=True)

        top_symbols_highest_positive = [
            symbol_data for symbol_data in sorted_data if symbol_data['avgInOI'] > 0][:10]

        symbols_highest_positive = [symbol_data['symbol']
                                    for symbol_data in top_symbols_highest_positive]
        avgInOI_values_highest_positive = [
            symbol_data['avgInOI'] for symbol_data in top_symbols_highest_positive]

        chart_data = ChartData(data_json=json.dumps(data))
        chart_data.save()

        context = {
            'symbols_lowest': symbols_lowest,
            'avgInOI_values_lowest': avgInOI_values_lowest,
            'symbols_highest_positive': symbols_highest_positive,
            'avgInOI_values_highest_positive': avgInOI_values_highest_positive,
            'symbols': symbols,
            'gain_percentages': gain_percentages,
               'symbols_losers': symbols,
        'loss_percentages': loss_percentages,
        }

        # Render the template
        return render(request, 'dashboard.html', context)
    else:

        chart_data = ChartData.objects.last()
        if chart_data:
            data = json.loads(chart_data.data_json)

            sorted_data = sorted(data['data'], key=lambda x: x['avgInOI'])

            top_symbols_lowest = sorted_data[:10]

            symbols_lowest = [symbol_data['symbol']
                              for symbol_data in top_symbols_lowest]
            avgInOI_values_lowest = [symbol_data['avgInOI']
                                     for symbol_data in top_symbols_lowest]

            sorted_data = sorted(
                data['data'], key=lambda x: x['avgInOI'], reverse=True)

            top_symbols_highest_positive = [
                symbol_data for symbol_data in sorted_data if symbol_data['avgInOI'] > 0][:10]

            symbols_highest_positive = [symbol_data['symbol']
                                        for symbol_data in top_symbols_highest_positive]
            avgInOI_values_highest_positive = [
                symbol_data['avgInOI'] for symbol_data in top_symbols_highest_positive]

            context = {
                'symbols_lowest': symbols_lowest,
                'avgInOI_values_lowest': avgInOI_values_lowest,
                'symbols_highest_positive': symbols_highest_positive,
                'avgInOI_values_highest_positive': avgInOI_values_highest_positive,
                'symbols': symbols,
                'gain_percentages': gain_percentages,
                   'symbols_losers': symbols,
        'loss_percentages': loss_percentages,
            }
            return render(request, 'dashboard.html', context)
        else:
            return HttpResponse("No data available.")


def help_support(request):
    return render(request, "help_support.html")


def learning_center(request):
    return render(request, "learning_center.html")


def blog(request):
    return render(request, "blog.html")


def my_strategies(request):
    return render(request, "my_strategies.html")


def my_portfolio(request):
    return render(request, "my_portfolio.html")


def broking_details(request):
    return render(request, "broking_details.html")


def courses_details(request):
    return render(request, "courses_details.html")


def reset_password(request):
    return render(request, "reset_password.html")


def Open_interest_analysis(request):
    if request.method == "POST":
        symbol = request.POST['symbols']
        expiry_dates = request.POST["expiryDates"]
        print(symbol, expiry_dates)
        if expiry_dates == "":
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
            datashort = dataopt.head(100)
            json_records = datashort.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            return render(request, "Open_interest_analysis.html", {"dataframe": data})

        else:
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
            return render(request, 'Open_interest_analysis.html', {"dataframe": data_filter})

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
    return render(request, "Open_interest_analysis.html", {"dataframe": data})


def signUp(request):
    if request.method == "POST":
        fname = request.POST["name"]
        email = request.POST["email"]
        phone_code = request.POST["phone_code"]
        mobile = request.POST["mobile"]
        country_id = request.POST.get("country_id", "")
        state_id = request.POST.get("state_id", "")
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
    return render(request, 'home.html')


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


def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        if User.objects.filter(email=email):
            token = str(uuid.uuid4())
            profile_email = User.objects.get(email=email)
            profile_email.forget_password_token = token
            profile_email.save()
            send_forget_password_mail(email, token)
            messages.success(
                request, 'An email has been sent you to ,please check the mail box')
            return redirect('/')

        else:
            messages.success(request, 'Sorry your email is not registered')
            return redirect('/')

    return render(request, 'reset_password.html')


def change_pass(request, token):

    profile_email = User.objects.filter(
        forget_password_token=token).first()

    print(profile_email)
    context = {'user_id': profile_email.id}

    if request.method == 'POST':
        l_pass = request.POST['new_pass']
        cpass = request.POST['confirm_pass']
        user_id = request.POST.get('user_id')
        print(l_pass, cpass)

        if l_pass != cpass:
            messages.error(request, 'both should  be equal.')
            return redirect(f'/change_pass/{token}/')

        else:
            change_pass = User.objects.get(id=user_id)
            change_pass.password = l_pass
            change_pass.confirm_password = cpass
            change_pass.set_password(l_pass)
            change_pass.save()
            messages.success(request, 'Your password has been changed.')

            return redirect('/')

    return render(request, 'change_pass.html', context)


def get_option_chain(request):
    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        if symbol == 'NIFTY':
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        elif symbol == 'BANKNIFTY':
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
        else:
            return JsonResponse({'success': False, 'message': 'Invalid symbol'})

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            option_data = response.json()
            expiry_dates = option_data['records']['expiryDates']
            print(expiry_dates)
            return JsonResponse({'expiry_dates': expiry_dates})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'success': False, 'message': 'Error fetching option chain data'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


def tests(request):
    data = {
        "data": [
            {
                "Unnamed: 0": 0,
                "fivedayoichange": 8.76,
                "fivedaypricechange": -0.02,
                "futuresPrice": 18631.55,
                "ivchange": 3.36,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.93,
                "onedaypricechange": -0.42,
                "shorttermoutlook": "-",
                "ticker": "NIFTY",
                "volper": 60.71,
                "volumechange": 106.87
            },
            {
                "Unnamed: 0": 1,
                "fivedayoichange": 8.72,
                "fivedaypricechange": 0.02,
                "futuresPrice": 44117.95,
                "ivchange": -2.73,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.72,
                "onedaypricechange": -0.07,
                "shorttermoutlook": "-",
                "ticker": "BANKNIFTY",
                "volper": 68.25,
                "volumechange": 102.76
            },
            {
                "Unnamed: 0": 2,
                "fivedayoichange": 7.42,
                "fivedaypricechange": -1.81,
                "futuresPrice": 508.1,
                "ivchange": -2.2,
                "mediumtermoutlook": "-",
                "onedayoichange": 1.53,
                "onedaypricechange": -1.52,
                "shorttermoutlook": "-",
                "ticker": "AARTIIND",
                "volper": 10.71,
                "volumechange": 102.07
            },
            {
                "Unnamed: 0": 3,
                "fivedayoichange": -0.07,
                "fivedaypricechange": 2.89,
                "futuresPrice": 4138.05,
                "ivchange": -1.29,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.07,
                "onedaypricechange": 0.77,
                "shorttermoutlook": "-",
                "ticker": "ABB",
                "volper": 0.0,
                "volumechange": 78.52
            }
        ]
    }
    data1 = []
    for d in data["data"]:
        data1.append(d)

    return render(request, 'tests.html', {'data1': data1})


def Algo_market_place(request):
    return render(request, "Algo_market_place.html")
