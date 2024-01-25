import time
from playwright.sync_api import Page, expect



class BasePage(object):

    def __init__(self, page: Page):
        self.page = page


class PageMetod(BasePage):

    def __init__(self, page):
        super().__init__(page)


    def open_msk_rt_ru(self):
        url = self.page.goto('https://msk.rt.ru/')
        expect(self.page).to_have_url('https://msk.rt.ru/')
        return url.url

    """Метод возвращает Title страницы первые 10 сиmволов + сравнение playwright"""
    def title_msk_rt_ru(self):
        titles = self.page.title()
        expect(self.page).to_have_title("Ростелеком - официальный сайт для физических лиц. г. Москва. Услуги доступа в интернет, ТВ и телефонной связи.")
        return titles[0:10]

    """Метод принимает локатор для ссылок и возвращает текст ссылки и два УРЛ до нажатия и после"""
    def linc_head(self, locatorss):
        text = self.page.locator(f'{locatorss}').inner_text()
        url1 = self.page.url
        self.page.locator(f'{locatorss}').click()
        url2 = self.page.url
        return text, url1, url2

    """Вспомогательный метод Kлик"""
    def clik(self, locatorss):
        self.page.click(f'{locatorss}')

    """Достать текст из ......"""
    def text_from(self, locatorss):
        text = self.page.locator(f'{locatorss}').inner_text()
        return text

    """Вернуть Урл при открытии в другой вкладке c click"""
    def next_url_new_vkladka(self, locatorss):
        with self.page.expect_popup() as popup_info:
            self.page.locator(f'{locatorss}').click()
        popup = popup_info.value
        popup.wait_for_load_state()
        print(popup.title())
        return popup.url

    """Метод возвращает текущий URL"""
    def curent_url(self):
        url = self.page.url
        return url


    def mouse_hover(self, locatorss):
        self.page.locator(locatorss).hover()


    def locator(self, locatorss):
        self.page.locator(locatorss)


    def get_by_placeholder(self, locatorss):
        self.page.get_by_placeholder(locatorss)

    """Meтод get_by_placeholder  + fill"""

    def get_by_placeholder_fill(self, locatorss, loc):
        self.page.get_by_placeholder(locatorss).fill(loc)


    def get_by_placeholder_press(self, locatorss):
        self.page.get_by_placeholder(locatorss).press('Enter')


    def specific_hover_test_keys_21(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="с ТВ и онлайн-кинотеатром").hover()
        self.page.get_by_role("link", name="с ТВ и онлайн-кинотеатром").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_22(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="с ТВ и онлайн-кинотеатром").hover()
        self.page.get_by_role("link", name="с мобильной связью", exact=True).click()
        url = self.page.url
        return url


    def specific_hover_test_keys_23(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="с ТВ и онлайн-кинотеатром").hover()
        self.page.get_by_role("link", name="с мобильной связью", exact=True).hover()
        self.page.get_by_role("link", name="с ТВ, онлайн-кинотеатром и мобильной связью").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_24(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="с ТВ и онлайн-кинотеатром").hover()
        self.page.get_by_role("link", name="с мобильной связью", exact=True).hover()
        self.page.get_by_role("link", name="с ТВ, онлайн-кинотеатром и мобильной связью").hover()
        self.page.get_by_role("link", name="Все пакеты").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_25(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="Мобильная связь").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_26(self):
        self.page.get_by_text("Пакеты услуг", exact=True).hover()
        self.page.locator("span").filter(has_text="Домашний интернет").hover()
        self.page.get_by_role("link", name="Мобильная связь").hover()
        self.page.get_by_role("link", name="Переход со своим номером").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_28(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_29(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_30(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_31(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Интернет в частный дом").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_32(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Интернет в частный дом").hover()
        self.page.get_by_role("link", name="Антивирусы").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_33(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Интернет в частный дом").hover()
        self.page.get_by_role("link", name="Антивирусы").hover()
        self.page.get_by_role("link", name="Облачное хранилище").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_34(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Интернет в частный дом").hover()
        self.page.get_by_role("link", name="Антивирусы").hover()
        self.page.get_by_role("link", name="Облачное хранилище").hover()
        self.page.get_by_role("link", name="Родительский контроль").click()
        url = self.page.url
        return url


    def specific_hover_test_keys_35(self):
        self.page.get_by_role("banner").get_by_text("Интернет", exact=True).hover()
        self.page.get_by_role("link", name="Надежный интернет C").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Домашний интернет").hover()
        self.page.get_by_role("link", name="Тарифы для геймеров").hover()
        self.page.locator("#previewNav").get_by_role("link", name="Интернет в частный дом").hover()
        self.page.get_by_role("link", name="Антивирусы").hover()
        self.page.get_by_role("link", name="Облачное хранилище").hover()
        self.page.get_by_role("link", name="Родительский контроль").hover()
        self.page.get_by_role("link", name="Роутеры и модемы").click()
        url = self.page.url
        return url

    """МЕТОД как один из вариантов для ввода текста в строку геолокации"""
    def location_inpud(self):
        self.page.locator("#block-b2cpanellichnykhkabinetoviligeo a").click()
        self.page.get_by_placeholder("Найти город").fill("Балашиха")
        time.sleep(2)
        self.page.get_by_placeholder("Найти город").press("Enter")
        time.sleep(2)
        text = self.page.locator("#block-b2cpanellichnykhkabinetoviligeo a").inner_text()
        url = self.page.url
        return text, url






