#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:00:37 2023

@author: shbshka
"""
from aiogram import Bot, Dispatcher, executor, types
import tokenizer
from gensim.utils import simple_preprocess
import nest_asyncio
nest_asyncio.apply()

bot = Bot(token="5193982529:AAH1PsHOCJSEInB9DmkEgst6_vGF6PkrE6s")
dp = Dispatcher(bot)

vowels = ["а", "о", "у", "ы", "э", "я", "ё", "ю", "и", "е"]
lat_vowels = ["a", "e", "y", "u", "i", "o"]


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Напиши-хуяпиши мне-хуе что-нибудь-хуёнибудь")


@dp.message_handler(content_types=["text"])
async def reply_to_message(message: types.Message):
    sentences = []
    for sentence in tokenizer.split_into_sentences(message.text):
        sentences.append(simple_preprocess(sentence, deacc=True))
    answers = ""
    for sentence in sentences:
        for word in sentence:
            if word in '!@#$%^&*()_+-—=…?/`\|><,.':
                sentence.remove(word)
            new_word = [x for x in word]
            while not new_word[0] in vowels and not new_word[0] in lat_vowels:
                del new_word[0]

            for x in range(len(vowels)):
                if new_word == vowels[x]:
                    token = ""
                else:
                    token = "".join(new_word[1:])

            for y in range(len(lat_vowels)):
                if new_word == lat_vowels[y]:
                    token = ""
                else:
                    token = "".join(new_word[1:])

            if new_word[0] == "а" or new_word[0] == "я":
                answer = word + "-" + "хуя" + token
            elif new_word[0] == "о" or new_word[0] == "ё":
                answer = word + "-" + "хуё" + token
            elif new_word[0] == "у" or new_word[0] == "ю":
                answer = word + "-" + "хую" + token
            elif new_word[0] == "ы" or new_word[0] == "и":
                answer = word + "-" + "хуи" + token
            elif new_word[0] == "э" or new_word[0] == "е":
                answer = word + "-" + "хуе" + token
            elif new_word[0] == "a":
                answer = word + "-" + "huya" + token
            elif new_word[0] == "e":
                answer = word + "-" + "huye" + token
            elif new_word[0] == "y":
                answer = word + "-" + "huye" + token
            elif new_word[0] == "u":
                answer = word + "-" + "huyu" + token
            elif new_word[0] == "i":
                answer = word + "-" + "huya" + token
            elif new_word[0] == "o":
                answer = word + "-" + "hyuo" + token
            else:
                answer = word + "-" + "хуе" + token


            answers += (answer + " ")

    await bot.send_message(message.from_user.id, answers)

if __name__ == "__main__":
    executor.start_polling(dp)
