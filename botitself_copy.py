from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio
import os
from collections import defaultdict
import dataset
import config

search_flag = False
actor_flag = False
topic_flag = False
token = config.my_token
bot = AsyncTeleBot(token)

df = dataset.Dataset(config.data, config.smaller_data, config.credits, config.keywords)
markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
help_item = types.KeyboardButton(config.help_button)
search_item = types.KeyboardButton(config.search_button)
actor_item = types.KeyboardButton(config.actor_button)
topic_item = types.KeyboardButton(config.topic_button)
markup.add(search_item, actor_item, topic_item, help_item)

@bot.message_handler(commands=[config.start_command])
async def send_welcome_message(message):
    await bot.reply_to(message, config.say_hello,
                       reply_markup=markup)

@bot.message_handler(content_types=[config.type_content])
async def reply_commands(message):
    global search_flag
    global actor_flag
    global topic_flag
    if search_flag:
        search_flag = False
        res = df.rec_sim(message.text)
        await bot.reply_to(message, res)
    elif actor_flag:
        actor_flag = False
        res = df.rec_act(message.text)
        await bot.reply_to(message, res)
    elif topic_flag: 
        topic_flag = False
        res = df.rec_topic(message.text)
        await bot.reply_to(message, res)
    elif message.text == config.help_button:
        search_flag = False
        actor_flag = False
        topic_flag = False
        await bot.reply_to(message, config.help_reply)
    elif message.text == config.search_button:
        search_flag = True
        await bot.reply_to(message, config.search_reply)
    elif message.text == config.actor_button:
        actor_flag = True
        await bot.reply_to(message, config.actor_reply)
    elif message.text == config.topic_button:
        topic_flag = True
        await bot.reply_to(message, config.topic_reply)
asyncio.run(bot.polling())
