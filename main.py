from telebot import TeleBot, types
import asyncio
from src import config
from src import analizator

class FilmBot:
    def __init__(self, token):
        self.token = token
        self.bot = TeleBot(token)
        self.search_flag = False
        self.actor_flag = False
        self.topic_flag = False
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        self.help_item = types.KeyboardButton(config.help_button)
        self.search_item = types.KeyboardButton(config.search_button)
        self.actor_item = types.KeyboardButton(config.actor_button)
        self.topic_item = types.KeyboardButton(config.topic_button)
        self.markup.add(self.search_item, self.actor_item, self.topic_item, self.help_item)

        self.bot.message_handler(commands=[config.start_command])(self.send_welcome_message)
        self.bot.message_handler(content_types=[config.type_content])(self.reply_commands)

    def send_welcome_message(self, message):
        self.bot.reply_to(message, config.say_hello, reply_markup=self.markup)

    def reply_commands(self, message):
        command = message.text.lower()

        if command == config.help_button.lower() or command == config.command_help:
            self.search_flag = False
            self.actor_flag = False
            self.topic_flag = False
            self.bot.reply_to(message, config.help_reply)
        elif command == config.search_button.lower() or command == config.command_search:
            self.search_flag = True
            self.bot.reply_to(message, config.search_reply)
        elif command == config.actor_button.lower() or command == config.command_actor:
            self.actor_flag = True
            self.bot.reply_to(message, config.actor_reply)
        elif command == config.topic_button.lower() or command == config.command_topic:
            self.topic_flag = True
            self.bot.reply_to(message, config.topic_reply)
        else:
            if self.search_flag:
                self.search_flag = False
                res = asyncio.run(analizator.Parser().rec_sim(message.text))
                self.bot.reply_to(message, res)
            elif self.actor_flag:
                self.actor_flag = False
                res = asyncio.run(analizator.Parser().rec_act(message.text))
                self.bot.reply_to(message, res)
            elif self.topic_flag: 
                self.topic_flag = False
                res = asyncio.run(analizator.Parser().rec_topic(message.text))
                self.bot.reply_to(message, res)

    def run(self):
        self.bot.polling()

if __name__ == '__main__':
    bot = FilmBot(config.my_token)
    bot.run()
