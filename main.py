import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# On récupère le token Telegram depuis les variables d'environnement Railway
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

def start(update, context):
    """Répond à la commande /start."""
    update.message.reply_text("Bienvenue dans YouGame ! Ton bot fonctionne correctement.")

def echo(update, context):
    """Répond à tous les autres messages texte."""
    user_text = update.message.text
    update.message.reply_text(f"Tu as écrit : {user_text}")

def main():
    # Création du bot avec le token
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher

    # Handler pour /start
    dp.add_handler(CommandHandler("start", start))

    # Handler pour tous les messages texte non-commandes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Lancement du bot (long polling)
    updater.start_polling()
    updater.idle()

# Point d'entrée du script
if __name__ == "__main__":
    main()
