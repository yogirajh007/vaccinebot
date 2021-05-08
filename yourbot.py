import requests
import json
import sys, getopt
import pprint
from datetime import date,timedelta,datetime
import telebot
import time
bot = telebot.TeleBot("Enter Telegram API Key")



datass = """Select district by number:
391 Ahmednagar
364 Akola
366 Amravati
397 Aurangabad
384 Beed
370 Bhandara
367 Buldhana
380 Chandrapur
388 Dhule
379 Gadchiroli
378 Gondia
386 Hingoli
390 Jalgaon
396 Jalna
371 Kolhapur
383 Latur
395 Mumbai
365 Nagpur
382 Nanded
387 Nandurbar
389 Nashik
381 Osmanabad
394 Palghar
385 Parbhani
363 Pune
393 Raigad
372 Ratnagiri
373 Sangli
376 Satara
374 Sindhudurg
375 Solapur
392 Thane
377 Wardha
369 Washim
368 Yavatmal"""


print(datass)

cid = "ENTER YOUR CID WITHOUT QUOTES HERE"

district = int(input())
while True:
    start_date = date.today()
    newss = ""
    datenow = start_date.strftime("%d-%m-%Y")
    print(datenow)
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(district)+'&date='+datenow)
    jsonr = response.json()
    sur = {}
    data = jsonr['centers']
    for center in data:
        avl = 0
        flag = 0
        sessions = center['sessions']
        for session in sessions:
            if session['min_age_limit'] != 45:
                flag = 1
                #if center['center_id'] == 583116:
                avl = avl + int(session['available_capacity'])
                sesdate = session['date']
        if flag == 1:
            if avl == 0:
                tp = "\t {:<25}".format(center['name']) + '\t Available : ' + str(avl) 
                #bot.send_message(781902529, tp)
                newss = newss + tp
            else:
                tp = "\t {:<25}".format(center['name']) + '\t Available : ' + str(avl) + ' on ' + sesdate 
                bot.send_message(cid, tp)
    #bot.send_message(781902529, newss)
    print(datetime.now())
    time.sleep(60)
