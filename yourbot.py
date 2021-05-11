import requests
import json
import sys, getopt
import pprint
from datetime import date,timedelta,datetime
import telebot
import time
bot = telebot.TeleBot("Enter Telegram bot token")

nowdate = date.today().strftime("%d-%m-%Y")
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }


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

def daterange(n):
    hh = [0]
    for i in hh:
        start_date = date.today()
        yield start_date + timedelta(i)

print(datass)

cid = "ENTER YOUR CID WITHOUT QUOTES HERE"
oldtp = ""
district = int(input())
while True:
    try:
        for single_date in daterange(10):
            newss = ""
            datenow = single_date.strftime("%d-%m-%Y")
            print(datenow)
            response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(district)+'&date='+datenow , headers=headers)
            jsonr = response.json()
            data = jsonr['centers']
            for center in data:
                if PINCODE1 < center['pincode'] < PINCODE2:   #Replace PINCODES
                    sessions = center['sessions']
                    for session in sessions:
                        if session['min_age_limit'] != 45 and session['available_capacity'] > 0:
                            avl = int(session['available_capacity'])
                            sesdate = session['date']
                            tp = "\t {:<25}".format(center['name']) + '\t Available : ' + str(avl) + ' on ' + sesdate
                            print(tp)
                            if oldtp!=tp :
                                bot.send_message(cid, tp)
                                oldtp = tp
            print(datetime.now())
    except Exception as e:
        print(e)
    time.sleep(60)
