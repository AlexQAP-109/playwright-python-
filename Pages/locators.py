"""ЛОКАТОРЫ ДЛЯ страницы https://msk.rt.ru/"""



"""ШАПКА СТРАНИЦЫ"""
link_dla_biznes = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[1]/a[2]/span[1]'

link_dla_mena = 'xpath=//*[@id="block-b2bverkhneemenyusegmentovnovoe"]/div/div/div/div/div[1]/a[1]'

link_dla_operatorov = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[1]/a[3]'

linc_blog = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[1]/a[4]'

tri_tochki ='xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div'

link_o_kompani = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[1]'

link_dla_partnerov = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[2]'

link_dla_investorov = 'xpath=//*[@id="block-b2cshapkaverkhneemenyusegmentyitelefony"]/div/div/div[1]/div/div[2]/div[2]/a[3]'

link_help = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[1]/a[1]'

link_bonus = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[1]/a[2]'

link_oplata = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[1]/div[1]'

spisok = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[2]'

linc_uslugi_rostelecom = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[2]/a[1]'

linc_perevod_s_kartu = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[2]/a[2]'

linc_oplata_drugih_org = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[2]/a[3]'

linc_poisk_plateja = 'xpath=//*[@id="block-b2cverkhneemenyuvozlelogotipanovoe"]/div/div/div/div[2]/div[2]/a[4]'

button_voyti = 'xpath=//*[@id="short-name-block-id"]/button'

spisok_voyti = 'xpath=//*[@id="lk-enter"]/div[2]/div[2]/div'

link_auth_rostelecom_moskva = 'xpath=//*[@id="lk-enter"]/div[2]/div[2]/div/div[1]/a'

link_auth_lichnuy_kabinet = 'xpath=//*[@id="lk-enter"]/div[2]/div[2]/div/div[2]/a'

link_auth_umniy_dom = 'xpath=//*[@id="lk-enter"]/div[2]/div[2]/div/div[3]/a'

spisok_paketu_uslug = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div'

link_s_tv_i_onlain = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[1]/div[2]/div/a'

link_s_mobil_svyas = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[1]/div[3]/div/a'

link_s_tv_onlin_kinoteatr ='xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[1]/div[4]/div/a'

link_vse_paketi = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[1]/div[5]/div/a'

link_mobilnaya_svyaz = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/a'

lynk_perehodi_so_svoim_nomerom = 'xpath=//*[@id="previewNav"]/div[1]/div/div/div/div/div/div[2]/div[3]/div[1]/a'



"""ВЫПАДАЮЩИЙ СПИСОК ИНТЕРНЕТ В ШАПКЕ СТРАНИЦИ"""
spisok_internet = 'xpath=//*[@id="previewNav"]/div[2]/div/div'


"""Локаторы из выпадающего списка Интернет"""
# get_by_role("banner").get_by_text("Интернет", exact=True)
# get_by_role("link", name="Надежный интернет C")
# locator("#previewNav").get_by_role("link", name="Домашний интернет")
# get_by_role("link", name="Тарифы для геймеров")
# locator("#previewNav").get_by_role("link", name="Интернет в частный дом")
# get_by_role("link", name="Антивирусы")
# get_by_role("link", name="Облачное хранилище")
# get_by_role("link", name="Родительский контроль")
# get_by_role("link", name="Роутеры и модемы")

link_nadejnuy_internet_s = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[1]/a/div[2]/div[1]'

link_domachniy_internet = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/a'

link_tarif_dla_geymerov = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/a'

link_internet_v_chasnuy_dom = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/a'

link_antivirusi = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/a'

link_oblachnoe_hranilische = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/a'

link_roditelskiy_control = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/a'

link_router_i_modem = 'xpath=//*[@id="previewNav"]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/a'


"""LOCACION"""
button_header_location = 'xpath=//*[@id="block-b2cpanellichnykhkabinetoviligeo"]/div/a/span'

forma_location_text = "Выбор города подключения"

inpud_naiti_gorod = 'Найти город'

fill_gorod = 'Балашиха'




