import os
import telebot

# Récupérer le token Telegram depuis les variables Railway
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(
        message,
        "Bienvenue dans YouGame ! Ton bot fonctionne correctement."
    )

@bot.message_handler(func=lambda msg: True)
def handle_all(message):
    # Réponse simple pour vérifier que tout marche
    bot.reply_to(message, f"Tu as dit : {message.text}")

if _name_ == "_main_":
    print("Bot YouGame démarré…")
    bot.infinity_polling(skip_pending=True)
