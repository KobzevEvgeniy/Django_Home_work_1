from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def text(title, text):
    return f'<h1>Добро пожаловать на сайт FIRSAPP</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'


def main_page(request):
    title = 'Главная страница сайта'
    body_text = 'Вы попали на сайт созданный с помощью фреймворка Django'
    logger.info(f'Page "main" is open')
    return HttpResponse(text(title, body_text))


def about_me(request):
    title = 'О себе'
    body_text = 'Кобзев Евгений Васильевич, студент Gegbrains<br>' \
                'Начал обучение в 2022 году по программе "Цифровые профессии" по специальности Программист Пайтон'
    logger.info(f'Page "about_me" is open')
    return HttpResponse(text(title, body_text))



