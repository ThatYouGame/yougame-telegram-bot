mport os
import telebot

# Récupération des tokens depuis Railway
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bienvenue dans YouGame ! Ton bot fonctionne correctement.")

# Boucle principale
if _name_ == "_main_":
    print("Bot YouGame lancé...")
    bot.infinity_polling()
