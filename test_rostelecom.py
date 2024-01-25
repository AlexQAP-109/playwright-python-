import time
from Pages.locators import *


def test_keys_1(start):
    """В тесте используем фикстуру  start инициализируем класс и передаем URL обращаемся к методу"""
    url = start.open_msk_rt_ru()
    titles = start.title_msk_rt_ru()
    print(f'Ростелеком == {titles}')
    assert titles == 'Ростелеком'
    print(f'{url} == https://msk.rt.ru/')
    assert url == 'https://msk.rt.ru/'


def test_keys_2(start):
    """При переходах по ссылкам через метод возвращаем URL и текст ссылки - сравниваем результаты"""
    text, url1, url2 = start.linc_head(link_dla_biznes)
    print(f'Tекст ссылки Для бизнеса == {text}')
    assert text == 'Для бизнеса'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_3(start):
    """Так как начальная страница по дефолту https://msk.rt.ru/ Для меня - осуществим два перехода
    c помощью f '' строки передаем локатор в метод"""
    text, url1, url2 = start.linc_head(link_dla_biznes)
    text2, url3, url4 = start.linc_head(link_dla_mena)
    print(f'{url1} != {url2}')
    assert url1 != url2
    print(f'{url3} != {url4}')
    assert url3 != url4
    print(f'Tекст ссылки Для бизнеса == {text}')
    assert text == 'Для бизнеса'
    print(f'Tекст ссылки Для бизнеса == {text2}')
    assert text2 == 'Для меня'


def test_keys_4(start):
    """Проверка ссылки 'Для операторов'"""
    text, url1, url2 = start.linc_head(link_dla_operatorov)
    print(f'Tекст ссылки Для операторов == {text}')
    assert text == 'Для операторов'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_5(start):
    """Проверка ссылки 'Блог'"""
    text, url1, url2 = start.linc_head(linc_blog)
    print(f'Tекст ссылки Блог == {text}')
    assert text == 'Блог'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_6(start):
    """Проверка ссылки 'О компании'. Используем вспомогательный метод clik для открытия
    меню три точки"""
    start.clik(tri_tochki)
    text, url1, url2 = start.linc_head(link_o_kompani)
    print(f'Tекст ссылки О компании == {text}')
    assert text == 'О компании'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_7(start):
    """Проверка ссылки 'Для партнёров'. Используем вспомогательный метод clik для открытия
    меню три точки"""
    start.clik(tri_tochki)
    text, url1, url2 = start.linc_head(link_dla_partnerov)
    print(f'Tекст ссылки Для партнёров == {text}')
    assert text == 'Для партнёров'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_8(start):
    """Проверка ссылки 'Для инвесторов'. Используем вспомогательный метод clik для открытия
    меню три точки"""
    start.clik(tri_tochki)
    text, url1, url2 = start.linc_head(link_dla_investorov)
    print(f'Tекст ссылки Для инвесторов == {text}')
    assert text == 'Для инвесторов'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_9(start):
    """Проверка ссылки 'Помощь'"""
    text, url1, url2 = start.linc_head(link_help)
    print(f'Tекст ссылки Помощь == {text}')
    assert text == 'Помощь'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_10(start):
    """Проверка ссылки 'Бонусы'"""
    text, url1, url2 = start.linc_head(link_bonus)
    print(f'Tекст ссылки Бонусы == {text}')
    assert text == 'Бонусы'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys11(start):
    """Кнопка с выпадающим списком Оплата. Кликаем и забираем текст. Так же
    забираем текст из выпавшего списка с ссылками"""
    start.clik(link_oplata)
    text = start.text_from(link_oplata)
    text2 = start.text_from(spisok)
    print(f'кнопка Оплата == {text}')
    assert text == 'Оплата'
    print(f'Выпадающий список == {text2}')
    assert text2 == 'Услуги Ростелекома\n''Перевод с карты на карту\n''Оплата других организаций\n''Поиск платежа'


def test_keys_12(start):
    """Проверка ссылки 'Услуги Ростелекома'"""
    start.clik(link_oplata)
    text, url1, url2 = start.linc_head(linc_uslugi_rostelecom)
    print(f'Tекст ссылки Услуги Ростелекома == {text}')
    assert text == 'Услуги Ростелекома'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_13(start):
    """Проверка ссылки 'Перевод с карты на карту'"""
    start.clik(link_oplata)
    text, url1, url2 = start.linc_head(linc_perevod_s_kartu)
    print(f'Перевод с карты на карту == {text}')
    assert text == 'Перевод с карты на карту'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_14(start):
    """Проверка ссылки 'Оплата других организаций'"""
    start.clik(link_oplata)
    text, url1, url2 = start.linc_head(linc_oplata_drugih_org)
    print(f'Оплата других организаций == {text}')
    assert text == 'Оплата других организаций'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_15(start):
    """Проверка ссылки 'Поиск платежа'"""
    start.clik(link_oplata)
    text, url1, url2 = start.linc_head(linc_poisk_plateja)
    print(f'Поиск платежа == {text}')
    assert text == 'Поиск платежа'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys16(start):
    """Кнопка с выпадающим списком Войти. Кликаем и забираем текст. Так же
    забираем текст из выпавшего списка с ссылками"""
    start.clik(button_voyti)
    text = start.text_from(button_voyti)
    text2 = start.text_from(spisok_voyti)
    print(f'кнопка Войти == {text}')
    assert text == 'Войти'
    print(f'Выпадающий список == {text2}')
    assert text2 == 'Ростелеком Москва\n\n''Личный кабинет РФ\n\n''Умный дом'


def test_keys_17(start):
    """Проверка ссылки 'Ростелеком Москва'"""
    start.clik(button_voyti)
    url1 = start.curent_url()
    text = start.text_from(link_auth_rostelecom_moskva)
    url2 = start.next_url_new_vkladka(link_auth_rostelecom_moskva)
    print(f'Ростелеком Москва == {text}')
    assert text == 'Ростелеком Москва'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_18(start):
    """Проверка ссылки 'Личный кабинет РФ'"""
    start.clik(button_voyti)
    url1 = start.curent_url()
    text = start.text_from(link_auth_lichnuy_kabinet)
    url2 = start.next_url_new_vkladka(link_auth_lichnuy_kabinet)
    print(f'Личный кабинет РФ == {text}')
    assert text == 'Личный кабинет РФ'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_19(start):
    """Проверка ссылки 'Умный дом''"""
    start.clik(button_voyti)
    url1 = start.curent_url()
    text = start.text_from(link_auth_umniy_dom)
    url2 = start.next_url_new_vkladka(link_auth_umniy_dom)
    print(f'Умный дом == {text}')
    assert text == 'Умный дом'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_20(start):
    """Забираем текст ссылок из пакета услуг"""
    text = start.text_from(spisok_paketu_uslug)
    print(f'{text} == {text}')
    assert text == 'Домашний интернет с ТВ и онлайн-кинотеатром с мобильной связью с ТВ, ''онлайн-кинотеатром и мобильной связью Все пакеты Дополнительно Мобильная ''связь \n''              В пакете услуг\n''             Переход со своим номером \n''              В пакете услуг\n''            '


def test_keys_21(start):
    """Проверка ссылки 'с ТВ и онлайн-кинотеатром'. В тесте используем специальный метод для теста
    hover чтобы добраться до ссылки"""
    url1 = start.curent_url()
    text = start.text_from(link_s_tv_i_onlain)
    url2 = start.specific_hover_test_keys_21()
    print(f'с ТВ и онлайн-кинотеатром =={text}')
    assert text == 'с ТВ и онлайн-кинотеатром'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_22(start):
    """с мобильной связью"""
    url1 = start.curent_url()
    text = start.text_from(link_s_mobil_svyas)
    url2 = start.specific_hover_test_keys_22()
    print(f'с мобильной связью  =={text}')
    assert text == 'с мобильной связью'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_23(start):
    """с ТВ, онлайн-кинотеатром и мобильной связью"""
    url1 = start.curent_url()
    text = start.text_from(link_s_tv_onlin_kinoteatr)
    url2 = start.specific_hover_test_keys_23()
    print(f'с ТВ, онлайн-кинотеатром и мобильной связью  =={text}')
    assert text == 'с ТВ, онлайн-кинотеатром и мобильной связью'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_24(start):
    """Все пакеты"""
    url1 = start.curent_url()
    text = start.text_from(link_vse_paketi)
    url2 = start.specific_hover_test_keys_24()
    print(f'Все пакеты  =={text}')
    assert text == 'Все пакеты'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_25(start):
    """Мобильная связь"""
    url1 = start.curent_url()
    text = start.text_from(link_mobilnaya_svyaz)
    url2 = start.specific_hover_test_keys_25()
    print(f'Все пакеты  =={text}')
    assert text == 'Мобильная связь'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_26(start):
    """Переход со своим номером"""
    url1 = start.curent_url()
    text = start.text_from(lynk_perehodi_so_svoim_nomerom)
    url2 = start.specific_hover_test_keys_26()
    print(f'Переход со своим номером  == {text}')
    assert text == 'Переход со своим номером'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_27(start):
    """Забираем текст ссылок из выпадающего списка ИНТЕРНЕТ"""
    text = start.text_from(spisok_internet)
    print(f'{text} == {text}')
    assert text == 'Надежный интернетC умными системами мониторинга Домашний интернет Тарифы' \
                   ' для геймеров Интернет в частный дом Антивирусы Облачное хранилище Родительский' \
                   ' контроль Роутеры и модемы'


def test_keys_28(start):
    """Надежный интернет"""
    url1 = start.curent_url()
    text = start.text_from(link_nadejnuy_internet_s)
    url2 = start.specific_hover_test_keys_28()
    print(f'Надежный интернет  =={text}')
    assert text == 'Надежный интернет'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_29(start):
    """Домашний интернет"""
    url1 = start.curent_url()
    text = start.text_from(link_domachniy_internet)
    url2 = start.specific_hover_test_keys_29()
    print(f'Домашний интернет  =={text}')
    assert text == 'Домашний интернет'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_30(start):
    """Тарифы для геймеров"""
    url1 = start.curent_url()
    text = start.text_from(link_tarif_dla_geymerov)
    url2 = start.specific_hover_test_keys_30()
    print(f'Тарифы для геймеров  =={text}')
    assert text == 'Тарифы для геймеров'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_31(start):
    """Интернет в частный дом"""
    url1 = start.curent_url()
    text = start.text_from(link_internet_v_chasnuy_dom)
    url2 = start.specific_hover_test_keys_31()
    print(f'Интернет в частный дом  =={text}')
    assert text == 'Интернет в частный дом'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_32(start):
    """Антивирусы"""
    url1 = start.curent_url()
    text = start.text_from(link_antivirusi)
    url2 = start.specific_hover_test_keys_32()
    print(f'Антивирусы  =={text}')
    assert text == 'Антивирусы'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_33(start):
    """Облачное хранилище"""
    url1 = start.curent_url()
    text = start.text_from(link_oblachnoe_hranilische)
    url2 = start.specific_hover_test_keys_33()
    print(f'Облачное хранилище  =={text}')
    assert text == 'Облачное хранилище'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_34(start):
    """Родительский контроль"""
    url1 = start.curent_url()
    text = start.text_from(link_roditelskiy_control)
    url2 = start.specific_hover_test_keys_34()
    print(f'Родительский контроль  =={text}')
    assert text == 'Родительский контроль'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_35(start):
    """Роутеры и модемы"""
    url1 = start.curent_url()
    text = start.text_from(link_router_i_modem)
    url2 = start.specific_hover_test_keys_35()
    print(f'Роутеры и модемы  =={text}')
    assert text == 'Роутеры и модемы'
    print(f'{url1} != {url2}')
    assert url1 != url2


def test_keys_36(start):
    """Изменяем геолокацию с Москва на Балашиха"""
    url = start.curent_url()
    text = start.text_from(button_header_location)
    text1, url1 = start.location_inpud()
    print(f'{url} == {url}')
    assert url == 'https://msk.rt.ru/'
    print(f'{text} == {text}')
    assert text == 'Москва'
    print(f'{url1} == {url1}')
    assert url1 == 'https://mosoblast.rt.ru/-balashiha-'
    print(f'{text1} == {text1}')
    assert text1 == 'Балашиха'
    print(f'{url} != {url1}')
    assert url != url1
    print(f'{text} != {text1}')
    assert text != text1

def test_keys_37(start):
    """Изменяем геолокацию с Москва на Балашиха"""
    url = start.curent_url()
    text = start.text_from(button_header_location)
    start.clik(button_header_location)
    start.get_by_placeholder_fill(inpud_naiti_gorod, fill_gorod)
    time.sleep(2)
    start.get_by_placeholder_press(inpud_naiti_gorod)
    time.sleep(2)
    text1 = start.text_from(button_header_location)
    time.sleep(2)
    url1 = start.curent_url()
    print(f'{url} == {url}')
    assert url == 'https://msk.rt.ru/'
    print(f'{text} == {text}')
    assert text == 'Москва'
    print(f'{url1} == {url1}')
    assert url1 == 'https://mosoblast.rt.ru/-balashiha-'
    print(f'{text1} == {text1}')
    assert text1 == 'Балашиха'
    print(f'{url} != {url1}')
    assert url != url1
    print(f'{text} != {text1}')
    assert text != text1


