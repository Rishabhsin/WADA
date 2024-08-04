# WaDa Prohibited List Search Bot

This project is a Telegram bot that checks whether a given drug is listed in the World Anti-Doping Agency (WADA) prohibited list. The bot reads drug names from a file and matches them with user input.

## Features

- Responds to `/start` and `/help` commands with a welcome message.
- Checks user input against a list of prohibited drugs.
- Returns a warning message if the drug is found in the prohibited list.
- Advises consulting a doctor regardless of the search result.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `telebot` library
- A valid Telegram Bot API token

### Installation

1. Clone the repository or download the script files.
2. Install the required Python libraries using pip:

```bash
pip install pyTelegramBotAPI
```

3. Create a text file named `wada.txt` in the same directory as the script. This file should contain the list of prohibited drugs, one per line.

### Usage

1. Replace `"THIS IS A DEMO KEY"` in the script with your actual Telegram Bot API token.
2. Run the script:

```bash
python bot.py
```

3. Open Telegram and search for your bot by its name. Start a chat with it and enter drug names to see if they are prohibited.

### Example

User: `/start`

Bot: `WaDa prohibited list search. Please enter the drug name`

User: `aspirin`

Bot: `The drug you have mentioned, is not in the list of Wada's prohibited drugs. Please do consult a doctor before using it.`

## Script Details

### `bot.py`

```python
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
        return "The drug you have mentioned is prohibited by WADA.\n\nPlease do consult a doctor before using it. \n-----------------------------------------------\nHere is what I found...\n\n" + "\n".join(drugs)
    else:
        return "The drug you have mentioned is not in the list of WADA's prohibited drugs.\n\nPlease do consult a doctor before using it."

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "WaDa prohibited list search. Please enter the drug name")

@bot.message_handler(func=lambda message: len(message.text) > 3)
def get_text_messages(message):
    response = text_search(message)
    bot.reply_to(message, response or "No valid drug name provided")

bot.infinity_polling()
```

### Notes

- Ensure `wada.txt` is in the correct format and location.
- The bot uses regex to search for drug names in a case-insensitive manner.
- The script is set to continuously poll for new messages using `bot.infinity_polling()`.
