import pip
pip install python-telegram-bot
#pip.main(['3', 'install', 'telegram'])
#pip.main(['install', 'python-telegram-bot'])
#pip.main(['3', 'install', 'python-telegram-bot'])
#pip3.4 install  --user --upgrade future

from typing import Final
from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6900013318:AAHVBQY6d33kUkgpp_HGZrlwasfMVpX2XnE'
BOT_USERNAME: Final = '@Vantuc'



#Commands
async def gb_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Woodleigh GB')

#Response

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hi' in processed:
        return 'hello'
    
    return 'i dunno'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) ni {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

    #async def callback(update: Update, context: CallbackContext):


if __name__ == '__main__':
    print('Starting bot .....')
    app = Application.builder().token(TOKEN).build()

    #Commands
    #register_handler = CommandHandler('gb', gb_command, pass_args=True)

    app.add_handler(CommandHandler('gb', gb_command))


    #Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #error
    #app.add_error_handler(error)

    print('polling .....')
    app.run_polling(poll_interval=3)
