# -*- coding: utf-8 -*-

#Импорт библиотек
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

#Упрощение команды для сообщения
def msg(ui,message):
    vk.messages.send(
        peer_id=ui,
        random_id=get_random_id(),
        message=message
    )
#Упрощение команды для сообщения с клавиатурой(кнопками)
def msgkbrd(ui,message):
    global keyboard
    vk.messages.send(
        peer_id=ui,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=message
    )

#Функции для клавиатуры
def initk(): #создание клавиатуры
    global keyboard
    keyboard = VkKeyboard(one_time=False)
    
def greenk(t): #зелёная кнопка
    keyboard.add_button(t, color=VkKeyboardColor.POSITIVE)

def redk(t): #красная кнопка
    keyboard.add_button(t, color=VkKeyboardColor.NEGATIVE)

def bluek(t): #синяя кнопка
    keyboard.add_button(t, color=VkKeyboardColor.PRIMARY)

def whitek(t): #белая кнопка
    keyboard.add_button(t, color=VkKeyboardColor.DEFAULT)

def urlk(t, url): #кнопка с ссылкой
	keyboard.add_openlink_button(t, url)

def newlinek(): #новая строка
    keyboard.add_line()