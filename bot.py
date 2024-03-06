import telebot
import re

bot = telebot.TeleBot("THIS IS A DEMO KEY")

def text_search(message):
    substr = message.text.lower()
    drugs = []
    with open('wada.txt', 'r') as file:
        for line in file:
            if re.search(r'\b{}\b'.format(substr), line.lower()):
                drugs.append(line.rstrip())
    if drugs:
        return "The Drug you have mentioned is prohibited by WADA.\n\nPlease Do Consult a Doctor before using it. \n-----------------------------------------------\nHere is what I found...\n\n" + "\n".join(drugs)
    else:
        return "The drug you have mentioned, is not in the list of Wada's prohibited. Drugs\n\nPlease Do Consult a Doctor before using it."

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "WaDa prohibited list search. Please enter the drug name")

@bot.message_handler(func=lambda message: len(message.text) > 3)
def get_text_messages(message):
    response = text_search(message)
    bot.reply_to(message, response or "No valid drug name provided")

bot.infinity_polling()
