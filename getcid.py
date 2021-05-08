import requests
import json
import sys, getopt
import pprint
from datetime import date,timedelta,datetime
import telebot
import time
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN_HERE")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "This is your bot. Enter /getcid to get the cid.")


@bot.message_handler(commands=['getcid'])
def send_welcome(message):
        bot.reply_to(message, message.chat.id);


bot.polling()
