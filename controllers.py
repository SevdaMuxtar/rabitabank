from cProfile import run
from traceback import print_tb
from turtle import pos
from urllib import response

from flask import render_template, request, redirect, url_for, flash
from app import app
from models import *
import requests
from datetime import date, datetime, timedelta
import xmltodict
import json
from forms import OnlineQueueForm, OnlineDepositsForm
from models import *


@app.route('/home/')
def home():
    today = date.today().strftime('%d.%m.%Y')
    yesterday = (datetime.today() - timedelta(1)).strftime('%d.%m.%Y')
    rub_change = "const"
    eur_change = "const"
    gbp_change = "const"
    usd_change = "const"
    y_rub = 0
    y_eur = 0
    y_gbp = 0
    y_usd = 0
    t_rub = 0
    t_eur = 0
    t_gbp = 0
    t_usd = 0
    try:
        today_currency_response = requests.get(f'https://www.cbar.az/currencies/{today}.xml')
        yesterday_currency_response = requests.get(f'https://www.cbar.az/currencies/{yesterday}.xml')

        today_json = xmltodict.parse(today_currency_response.content)
        yesterday_json = xmltodict.parse(yesterday_currency_response.content)


        y_j_raw_data = yesterday_json['ValCurs']['ValType'][1]['Valute']
        t_j_raw_data = today_json['ValCurs']['ValType'][1]['Valute']

        for i in y_j_raw_data:
            if i['@Code'] == 'RUB' or i['@Code'] == 'EUR' or i['@Code'] == 'GBP' or i['@Code'] == 'USD':
                if i['@Code'] == 'RUB':
                    y_rub = i['Value']
                if i['@Code'] == 'EUR':
                    y_eur = i['Value']
                if i['@Code'] == 'GBP':
                    y_gbp = i['Value']
                if i['@Code'] == 'USD':
                    y_usd = i['Value']
                
        for i in t_j_raw_data:
            if i['@Code'] == 'RUB' or i['@Code'] == 'EUR' or i['@Code'] == 'GBP' or i['@Code'] == 'USD':
                if i['@Code'] == 'RUB':
                    t_rub = i['Value']
                if i['@Code'] == 'EUR':
                    t_eur = i['Value']
                if i['@Code'] == 'GBP':
                    t_gbp = i['Value']
                if i['@Code'] == 'USD':
                    t_usd = i['Value']

        if t_rub > y_rub:
            rub_change = "up"
        if t_rub < y_rub:
            rub_change = "down"

        if t_eur > y_eur:
            eur_change = "up"
        if t_eur < y_eur:
            eur_change = "down"

        if t_gbp > y_gbp:
            gbp_change = "up"
        if t_gbp < y_gbp:
            gbp_change = "down"

        if t_usd > y_usd:
            usd_change = "up"
        if t_usd < y_usd:
            usd_change = "down"
    except:
        print("Connecting error...")

    return render_template('header.html', rub=t_rub, eur=t_eur, gbp=t_gbp, usd=t_usd, rub_change=rub_change, eur_change=eur_change, gbp_change=gbp_change, usd_change=usd_change)
    
@app.route('/online-queue/', methods=['GET','POST'])
def online_queue():
    post_data = request.form
    form = OnlineQueueForm()
    if request.method == 'POST':
        form = OnlineQueueForm(data=post_data)
        if form.validate_on_submit():
            online_queue = OnlineQueue(filial_name_id=post_data.get("filial_name"), service_type_id=post_data.get("service_type"), date=post_data.get("date"), time_id=post_data.get("time"), phone_number=post_data.get("phone_number"))
            online_queue.save()
    return render_template('online-queue.html', form=form)

@app.route('/xeberler/<news_title>/')
def news_more(news_title):
    data = News.query.filter(News.title == news_title).all()
    return render_template('more-news.html',data=data)

@app.route('/xeberler/')
def news():
    active = "active"
    data = News.query.all()
    category_data = NewsCategory.query.all()
    return render_template('news.html', data=data,category_data=category_data, all_data=active)

@app.route('/xeberler/category/<category_name>/')
def news_category(category_name):
    data = News.query.all()
    active = category_name
    filter_data = []
    for i in data:
        if i.news_category.category_name == category_name:
            filter_data.append(i)

    category_data = NewsCategory.query.all()
    return render_template('news.html', data=filter_data, category_data=category_data, active=active)

# ------------------------------- MORE DEPOSTS ------------------------------- #

@app.route("/ferdi-musteriler/emanetler-az/<deposit_name>/")
def deposits_more(deposit_name):
    data = Deposits.query.all()
    features_data = DepositFeatures.query.all()
    response = requests.get('http://127.0.0.1:5000/api.rabite-bank/')
    response_json = response.json()
    filter_data = []
    filter_features_data = []
    for i in data:
        if i.deposit_name.deposit_name == deposit_name:
            filter_data.append(i)
    for j in features_data:
        if j.deposit_name.deposit_name == deposit_name:
            filter_features_data.append(j)



    return render_template("more-deposits.html", filter_data=filter_data[0], filter_features_data=filter_features_data[0], data=data)

# ------------------------------- MORE DEPOSITS ------------------------------ #

# ------------------------------------- - ------------------------------------ #

# --------------------------------- DEPOSITS --------------------------------- #

@app.route("/ferdi-musteriler/emanetler-az/", methods=['GET','POST'])
def deposits():
    data = Deposits.query.all()
    post_data = request.form
    form = OnlineDepositsForm()
    run = ""
    if request.method == 'POST':
        form = OnlineDepositsForm(data=post_data)
        if form.validate_on_submit():
            online_deposit = OnlineDeposit(name=post_data.get('name'), surname=post_data.get('surname'), phone_number=post_data.get('phone_number'), deposit_name_id=post_data.get('deposit_type'))
            online_deposit.save()
            form['name'].data = ""
            form['surname'].data = ""
            form['phone_number'].data = ""
            form['deposit_type'].data = ""
            run = 'runAlert()'
        else:
            run = 'notRunAlert()'
    return render_template("deposits.html", data=data, form=form, run=run)

# --------------------------------- DEPOSITS --------------------------------- #

# ------------------------------------- - ------------------------------------ #

# --------------------------------- CAMPAIGN --------------------------------- #

@app.route("/ferdi/kampaniyalar/")
def campaign():
    active = "active"
    data = Campaign.query.all()
    category_data = CampaignCategory.query.all()
    return render_template("campaign.html", data=data, category_data=category_data, all_data=active)

@app.route('/ferdi/kampaniyalar/<category_name>/')
def campaign_category(category_name):
    data = Campaign.query.all()
    active = category_name
    filter_data = []
    for i in data:
        if i.campaign_category.category_name == category_name:
            filter_data.append(i)

    category_data = CampaignCategory.query.all()
    return render_template('campaign.html', data=filter_data, category_data=category_data, active=active)

# --------------------------------- CAMPAIGN --------------------------------- #

# ------------------------------------- - ------------------------------------ #

# -------------------------------- CARD ORDER -------------------------------- #

@app.route("/ferdi/kartlar/kartmane-debet/", methods=['GET', 'POST'])
def order_card():
    card_types = CardType.query.all()
    card_currencies = CardCurrency.query.all()
    post_data = request.form.get
    if request.method == 'POST':

        if (post_data('card_type') == "" or post_data('card_type') == None) or (post_data('card_currency') == "" or post_data('card_currency') == None) or (post_data('firstname') == "" or post_data('firstname') == None) or (post_data('surname') == "" or post_data('surname') == None) or (post_data('phone') == "" or post_data('phone') == None) or (post_data('pid_code') == "" or post_data('pid_code') == None):
            flash("Xəta baş verdi, zəhmət olmasa yenidən cəhd edin.", "error")
        else:
            online_card_order = CardOrder(name=(post_data('firstname')), surname=(post_data('surname')), phone_number=(post_data('phone')), fin_code=(post_data('pid_code')), card_type_id=(post_data('card_type')), card_currency_id=(post_data('card_currency')))
            online_card_order.save()
            flash("Sorğunuz uğurla göndərildi.", 'success')


    return render_template("card-order.html", card_types=card_types, card_currencies=card_currencies)

# -------------------------------- CARD ORDER -------------------------------- #


@app.route('/api.rabite-bank/')
def api():
    dictionary = {
            "monthly": {
                "Tələb olunanadək": {
                    "azn": "-",
                    "usd": "-",
                    "eur": "-"
                },
                "3 ay": {
                    "azn": "-",
                    "usd": "-",
                    "eur": "-"
                },
                "6 ay": {
                    "azn": "4,00%",
                    "usd": "0,25%",
                    "eur": "-"
                },
                "12 ay": {
                    "azn": "9,25%",
                    "usd": "0,25%",
                    "eur": "-"
                },
                "24 ay": {
                    "azn": "9,50%",
                    "usd": "0,25%",
                    "eur": "-"
                },
                "36 ay": {
                    "azn": "9,50%",
                    "usd": "-",
                    "eur": "-"
                },
            },
            "quarterly": {
                "Tələb olunanadək": {
                    "azn": "1,00%",
                    "usd": "0,10%",
                    "eur": "0,05%"
                },
                "3 ay": {
                    "azn": "-",
                    "usd": "-",
                    "eur": "-"
                },
                "6 ay": {
                    "azn": "5,00%",
                    "usd": "0,35%",
                    "eur": "-"
                },
                "12 ay": {
                    "azn": "9,50%",
                    "usd": "0,35%",
                    "eur": "-"
                },
                "24 ay": {
                    "azn": "9,75%",
                    "usd": "0,35%",
                    "eur": "-"
                },
                "36 ay": {
                    "azn": "9,75%",
                    "usd": "-",
                    "eur": "-"
                },
            },
            "end-duration": {
                "Tələb olunanadək": {
                    "azn": "1",
                    "usd": "-",
                    "eur": "-"
                },
                "3 ay": {
                    "azn": "3,00%",
                    "usd": "-",
                    "eur": "-"
                },
                "6 ay": {
                    "azn": "6,00%",
                    "usd": "0,50%",
                    "eur": "-"
                },
                "12 ay": {
                    "azn": "10,00%",
                    "usd": "0,50%",
                    "eur": "0,50%"
                },
                "24 ay": {
                    "azn": "10,50%",
                    "usd": "0,50%",
                    "eur": "-"
                },
                "36 ay": {
                    "azn": "10,50%",
                    "usd": "-",
                    "eur": "-"
                },
            },
            "end-duration-2": {
                "0 - 30 gün": {
                    "azn": "0%",
                    "usd": "0%",
                    "eur": "0%"
                },
                "31 – 180 gün": {
                    "azn": "10%",
                    "usd": "10%",
                    "eur": "10%"
                },
                "181 – 360 gün": {
                    "azn": "20%",
                    "usd": "25%",
                    "eur": "25%"
                },
                "360 gündən sonra": {
                    "azn": "30%",
                    "usd": "50%",
                    "eur": "50%"
                }
            }
        }
    return dictionary
