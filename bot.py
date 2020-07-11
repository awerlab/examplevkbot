# -*- coding: utf-8 -*-

#Импорт библиотек
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import settings
import functions

#Добавление кнопок
functions.initk()
functions.greenk('зеленая кнопка')
functions.newlinek()
functions.bluek('синяя кнопка')
functions.urlk('Мы в гитхабе', 'github.comhetelber')

#Подключение к вк
token = settings.token
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
vk = vk.get_api()

#Отправка сообщений
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    m = event.text
                    m = m.lower()
                    if m == "привет":
                        functions.msg(event.user_id, 'Привет, как дела?')
                    elif m == "хорошо":
                        functions.msg(event.user_id, 'Круто, и у меня!')
                    if m == 'кнопки':
                        functions.msgkbrd(event.user_id, 'держи кнопочки')
    except:
        pass