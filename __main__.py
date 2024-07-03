#import telebot
#
#API_KEY = '7093567136:AAHvflgRH0cof6oW4FAzYlthpb8T3hbBak8'
#
#bot = telebot.TeleBot(API_KEY)
#
#@bot.message_handler(content_types=['text'])
#def hola(message):
#    print("hola")
#
#bot.polling()
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '7093567136:AAHvflgRH0cof6oW4FAzYlthpb8T3hbBak8'

async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_text = update.message.text

    print(f"Mensaje recibido de chat {chat_id}: {message_text}")

    # Responder al mensaje (opcional)
    await update.message.reply_text('Mensaje recibido')

def main():
    application = Application.builder().token(TOKEN).build()

    # Agregar manejador de mensajes de texto
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(text_handler)

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
