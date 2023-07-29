#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:00:37 2023

@author: shbshka
"""
from aiogram import Bot, Dispatcher, executor, types
import tokenizer
from gensim.utils import simple_preprocess
from config import TOKEN
import nest_asyncio
nest_asyncio.apply()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

vowels = ["а", "о", "у", "ы", "э", "я", "ё", "ю", "и", "е"]
lat_vowels = ["a", "e", "y", "u", "i", "o"]
lat_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Напиши-хуяпиши мне-хуе что-нибудь-хуёнибудь")


@dp.message_handler(content_types=["text"])
async def reply_to_message(message: types.Message):
    sentences = []
    sentence_words = []
    words = []
    text = message.text

    for sentence in tokenizer.split_into_sentences(text):
        sentences.append(sentence)

    for sentence in sentences:
        sentence_words.append(sentence.split(" "))

    for item in sentence_words:
        for word in item:
            word = word.lower()
            words.append(word)

    answers = ""
    for word in words:
        if word in '!@#$%^&*()_+-—=…?/`\|><,.\'\"':
            words.remove(word)

    for word in words:
        new_word = [x for x in word]
        try:
            while not new_word[0] in vowels and not new_word[0] in lat_vowels:
                del new_word[0]
        except IndexError:
            pass

        if new_word == [] and word[0] in lat_letters:
            answers += word + '-huye' + word + " "
        elif new_word == []:
            answers += word + '-хуе' + word + " "
        else:
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
                answer = word + "-" + "huyo" + token
            else:
                answer = word + "-" + "хуе" + token


            answers += (answer + " ")

    await bot.send_message(message.from_user.id, answers)

if __name__ == "__main__":
    executor.start_polling(dp)
