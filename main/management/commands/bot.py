from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        print("successfully running")
        bot.infinity_polling()
