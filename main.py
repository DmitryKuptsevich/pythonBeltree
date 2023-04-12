import time

import telebot
from telebot import types
import emoji
bot = telebot.TeleBot('5687768813:AAF6bvd3i8nad6eT9Hx2rLf0gOGCURnRoGY')
# Приветствие
@bot.message_handler(commands =['start'])
def start(message):
    bot.send_message(message.from_user.id,"\u270b""Привет!" "Я помогу тебе разобраться в нашей продукции")
    bot.send_message(message.from_user.id,"Ознакомиться с изделием можете в меню""\u2b07")
#Кнопки дачных туалетов
@bot.message_handler(content_types =['text'])
def get_text_messages(message):
    def webAppKeyboardKarkas():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppKarkas = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/karkas_tualeta_standart")
        one_butt = types.KeyboardButton(text="Подробнее",web_app=webAppKarkas)
        keyboard.add(one_butt)
        return keyboard

    def webAppKeyboardEkonom():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppEkonom = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/dachnyy_tualet_ekonom")
        two_butt = types.KeyboardButton(text="Подробнее", web_app=webAppEkonom)
        keyboard.add(two_butt)
        return keyboard

    def webAppKeyboardStandart():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppStandart = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy")
        three_butt = types.KeyboardButton(text="Подробнее", web_app=webAppStandart)
        keyboard.add(three_butt)
        return keyboard

    def webAppKeyboardBoks():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppBoks = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_boks")
        four_butt = types.KeyboardButton(text="Подробнее", web_app=webAppBoks)
        keyboard.add(four_butt)
        return keyboard

    def webAppKeyboardHouse():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouse = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_haus")
        five_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouse)
        keyboard.add(five_butt)
        return keyboard

    def webAppKeyboardDachny():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppDachny = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_s_pokraskoy")
        six_butt = types.KeyboardButton(text="Подробнее", web_app=webAppDachny)
        keyboard.add(six_butt)
        return keyboard

    def webAppKeyboardHata():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHata = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_hata")
        seven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHata)
        keyboard.add(seven_butt)
        return keyboard

    def webAppKeyboardHozjain():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHozjain = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_hozyain_bazovaya_model")
        eight_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHozjain)
        keyboard.add(eight_butt)
        return keyboard

    def webAppKeyboardHaspadar():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHaspadar = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_gaspadar")
        nine_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHaspadar)
        keyboard.add(nine_butt)
        return keyboard

    def webAppKeyboardUjut():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppUjut = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_uyut")
        ten_butt = types.KeyboardButton(text="Подробнее", web_app=webAppUjut)
        keyboard.add(ten_butt)
        return keyboard

    def webAppKeyboardHataDach():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHataDach = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_hata_1")
        eleven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHataDach)
        keyboard.add(eleven_butt)
        return keyboard

    def webAppKeyboardHozjainBlH():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHozjainBlH = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_hozyain_blokhaus")
        twelve_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHozjainBlH)
        keyboard.add(twelve_butt)
        return keyboard

    def webAppKeyboardOdnoklasny():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppOdnoklasny = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_odnoskatnyy")
        thirteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppOdnoklasny)
        keyboard.add(thirteen_butt)
        return keyboard

    def webAppKeyboardFantasy():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppFantasy = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/dachnyy_tualet_fantasia")
        fourteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppFantasy)
        keyboard.add(fourteen_butt)
        return keyboard

    def webAppKeyboardVolat():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppVolat = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/dachnyy_tualet_volat_bez_pokraski")
        fifteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppVolat)
        keyboard.add(fifteen_butt)
        return keyboard

    def webAppKeyboardSkazka2():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppSkazka2 = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_skazka_2")
        sixteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppSkazka2)
        keyboard.add(sixteen_butt)
        return keyboard

    def webAppKeyboardVolatColor():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppVolatColor = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/dachnyy_tualet_volat")
        seventeen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppVolatColor)
        keyboard.add(seventeen_butt)
        return keyboard

    def webAppKeyboardProstor():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppProstor = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_prostor")
        eightteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppProstor)
        keyboard.add(eightteen_butt)
        return keyboard

    def webAppKeyboardSkazka():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppSkazka = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_skazka")
        nineteen_butt = types.KeyboardButton(text="Подробнее", web_app=webAppSkazka)
        keyboard.add(nineteen_butt)
        return keyboard

    def webAppKeyboardTeremok():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppTeremok = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_teremok")
        twently_butt = types.KeyboardButton(text="Подробнее", web_app=webAppTeremok)
        keyboard.add(twently_butt)
        return keyboard

    def webAppKeyboardIzba():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppIzba = types.WebAppInfo("https://beltree.by/katalog_tovarov/tualety_dachnye/tualet_dachnyy_izba")
        twentlyOne_butt = types.KeyboardButton(text="Подробнее", web_app=webAppIzba)
        keyboard.add(twentlyOne_butt)
        return keyboard
# Кнопки колодцев
    def webAppKeyboardVorot():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppVorot = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/vorot_dlya_kolodca")
        twentlyTwo_butt = types.KeyboardButton(text="Подробнее", web_app=webAppVorot)
        keyboard.add(twentlyTwo_butt)
        return keyboard

    def webAppKeyboardHouseKol():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseKol = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/domik_dlya_kolodca")
        twentlyThree_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseKol)
        keyboard.add(twentlyThree_butt)
        return keyboard

    def webAppKeyboardHouseKolVorot():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseKolVorot = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/kolodec_s_vorotom")
        twentlyfour_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseKolVorot)
        keyboard.add(twentlyfour_butt)
        return keyboard

    def webAppKeyboardHouseKolSkazka():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseKolSkazka = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/domik_dlya_kolodca_skazka")
        twentlyfive_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseKolSkazka)
        keyboard.add(twentlyfive_butt)
        return keyboard

    def webAppKeyboardHouseKolTeremok():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseKolTeremok = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/domik_dlya_kolodca_teremok")
        twentlysix_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseKolTeremok)
        keyboard.add(twentlysix_butt)
        return keyboard

    def webAppKeyboardHouseKolClassic():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseKolClassic = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_kolodcev/kolodec_klassik")
        twentlyseven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseKolClassic)
        keyboard.add(twentlyseven_butt)
        return keyboard

# Будки для собак
    def webAppKeyboardHouseDogHoz():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogHoz = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobaki_hozyain")
        twentlyeight_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogHoz)
        keyboard.add(twentlyeight_butt)
        return keyboard

    def webAppKeyboardHouseDogStandart():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogStandart = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobaki_standart")
        twentlynine_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogStandart)
        keyboard.add(twentlynine_butt)
        return keyboard

    def webAppKeyboardHouseDogSharik():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogSharik = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobak_sharik")
        thirty_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogSharik)
        keyboard.add(thirty_butt)
        return keyboard

    def webAppKeyboardHouseDogRex():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogRex = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobaki_reks")
        thirtyone_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogRex)
        keyboard.add(thirtyone_butt)
        return keyboard

    def webAppKeyboardHouseDogTerassa():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogTerassa = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_s_terrasoy")
        thirtytwo_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogTerassa)
        keyboard.add(thirtytwo_butt)
        return keyboard

    def webAppKeyboardHouseDogAks():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogAks = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/sobachya_budkas_tamburom_aks")
        thirtythree_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogAks)
        keyboard.add(thirtythree_butt)
        return keyboard

    def webAppKeyboardHouseDogMinovoler():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogMinovoler = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_s_minivolerom")
        thirtyfour_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogMinovoler)
        keyboard.add(thirtyfour_butt)
        return keyboard

    def webAppKeyboardHouseDogMuhtar():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogMuhtar = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobaki_muhtar")
        thirtysix_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogMuhtar)
        keyboard.add(thirtysix_butt)
        return keyboard

    def webAppKeyboardHouseDogCheviz():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogCheviz = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/dvoynaya_budka_dlya_sobak_cheviz")
        thirtyseven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogCheviz)
        keyboard.add(thirtyseven_butt)
        return keyboard

    def webAppKeyboardHouseDogMonti():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogMonti = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobak_monti")
        thirtyeight_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogMonti)
        keyboard.add(thirtyeight_butt)
        return keyboard

    def webAppKeyboardHouseDogCesar():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogCesar = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_s_zakrytoy_terrasoy_cezar")
        thirtynine_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogCesar)
        keyboard.add(thirtynine_butt)
        return keyboard

    def webAppKeyboardHouseDogArchi():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogArchi = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_s_terrasoy_archi")
        fourty_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogArchi)
        keyboard.add(fourty_butt)
        return keyboard

    def webAppKeyboardHouseDogTamburAks():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogTamburAks = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_s_terrasoy_archi")
        fourtyone_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogTamburAks)
        keyboard.add(fourtyone_butt)
        return keyboard

    def webAppKeyboardHouseDogTamburLux():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseDogTamburLux = types.WebAppInfo("https://beltree.by/katalog_tovarov/budki_dlya_sobak/budka_dlya_sobaki_lyuks")
        fourtytwo_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseDogTamburLux)
        keyboard.add(fourtytwo_butt)
        return keyboard
# Домики для кошек
    def webAppKeyboardHouseCatStreet():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatStreet = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/zimniy_domik_dlya_kotov_ulichnyy")
        fourtythree_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatStreet)
        keyboard.add(fourtythree_butt)
        return keyboard

    def webAppKeyboardHouseCatStreetCl():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatStreetCl = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_kotov_ulichnyy")
        fourtyfour_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatStreetCl)
        keyboard.add(fourtyfour_butt)
        return keyboard

    def webAppKeyboardHouseCatBegemot():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatBegemot = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_dvorovyh_kotov_begemot")
        fourtyfive_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatBegemot)
        keyboard.add(fourtyfive_butt)
        return keyboard

    def webAppKeyboardHouseCatKorzhik():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatKorzhik = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/zimniy_domik_dlya_kotov_korzhik")
        fourtysix_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatKorzhik)
        keyboard.add(fourtysix_butt)
        return keyboard


    def webAppKeyboardHouseCatNozhki():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatNozhki = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/zimniy_domik_dlya_kotov_korzhik")
        fourtyseven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatNozhki)
        keyboard.add(fourtyseven_butt)
        return keyboard

    def webAppKeyboardHouseCatKompot():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatKompot = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_ulichnyh_kotov_kompot")
        fourtyeight_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatKompot)
        keyboard.add(fourtyeight_butt)
        return keyboard

    def webAppKeyboardHouseCatPushok():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatPushok = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/uteplennyy_domik_dlya_kotov_pushok")
        fourtynine_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatPushok)
        keyboard.add(fourtynine_butt)
        return keyboard

    def webAppKeyboardHouseCatTreuhol():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatTreuhol = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/budka_dlya_kotov_treugolnik")
        fivety_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatTreuhol)
        keyboard.add(fivety_butt)
        return keyboard

    def webAppKeyboardHouseCatBarsik():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatBarsik = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_kotov_barsik")
        fivetyone_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatBarsik)
        keyboard.add(fivetyone_butt)
        return keyboard

    def webAppKeyboardHouseCatVilla():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatVilla = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_koshek_villa")
        fivetytwo_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatVilla)
        keyboard.add(fivetytwo_butt)
        return keyboard

    def webAppKeyboardHouseCat2Level():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCat2Level = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_kotov_dvuhurovnevyy")
        fivetythree_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCat2Level)
        keyboard.add(fivetythree_butt)
        return keyboard

    def webAppKeyboardHouseCatTom():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatTom = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_kotov_tom")
        fivetyfour_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatTom)
        keyboard.add(fivetyfour_butt)
        return keyboard

    def webAppKeyboardHouseCotTaghe():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCotTaghe = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/budka_dlya_kotov_kottedzh")
        fivetysix_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCotTaghe)
        keyboard.add(fivetysix_butt)
        return keyboard

    def webAppKeyboardHouseCatHera():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatHera = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/uteplennyy_domik_dlya_koshek_gera")
        fivetyseven_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatHera)
        keyboard.add(fivetyseven_butt)
        return keyboard

    def webAppKeyboardHouseCatPethaus():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatPethaus = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/domik_dlya_kotov_pethaus")
        fivetyeight_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatPethaus)
        keyboard.add(fivetyeight_butt)
        return keyboard

    def webAppKeyboardHouseCatSkandi():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppHouseCatSkandi = types.WebAppInfo("https://beltree.by/katalog_tovarov/domiki_dlya_koshek/zimniy_domik_dlya_ulichnyh_kotov_skandi")
        fivetynine_butt = types.KeyboardButton(text="Подробнее", web_app=webAppHouseCatSkandi)
        keyboard.add(fivetynine_butt)
        return keyboard
# Летние души

    def webAppKeyboardDushUjut():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppDushUjut = types.WebAppInfo("https://beltree.by/katalog_tovarov/letnie_dushi_dlya_dachi/dushevaya_kabinka_uyut")
        sixty_butt = types.KeyboardButton(text="Подробнее", web_app=webAppDushUjut)
        keyboard.add(sixty_butt)
        return keyboard

    def webAppKeyboardDrovnicaPiramida():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppDrovnicaPiramida = types.WebAppInfo("https://beltree.by/katalog_tovarov/drovnicy/drovnik_piramida")
        sixtyone_butt = types.KeyboardButton(text="Подробнее", web_app=webAppDrovnicaPiramida)
        keyboard.add(sixtyone_butt)
        return keyboard

    def webAppKeyboardDrovnicaStandart():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppDrovnicaStandart = types.WebAppInfo("https://beltree.by/katalog_tovarov/drovnicy/drovnica_standart")
        sixtytwo_butt = types.KeyboardButton(text="Подробнее", web_app=webAppDrovnicaStandart)
        keyboard.add(sixtytwo_butt)
        return keyboard


    def webAppKeyboardDrovnicaHozblok():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        webAppDrovnicaHozblok = types.WebAppInfo("https://beltree.by/katalog_tovarov/drovnicy/drovnica_s_hozblokom")
        sixtythree_butt = types.KeyboardButton(text="Подробнее", web_app=webAppDrovnicaHozblok)
        keyboard.add(sixtythree_butt)
        return keyboard






# Дачные туалеты
    if message.text == '/command1':

        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/karkas-800x800.jpg"),reply_markup = webAppKeyboardKarkas())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/ekonom/ekonom-228x228.jpg"),reply_markup= webAppKeyboardEkonom())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/standart/standart-ti-brus-850x850.jpg"),reply_markup=webAppKeyboardStandart())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/boks/beks-bez-z-800x800.jpg"),reply_markup=webAppKeyboardBoks())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/haus/haus-850x850.jpg"),reply_markup=webAppKeyboardHouse())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/boks-pokraska-850x850.jpg"),reply_markup=webAppKeyboardDachny())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/hata/hata-120-850x850.jpg"),reply_markup=webAppKeyboardHata())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/hozjaion-bel-850x850.jpg"),reply_markup=webAppKeyboardHozjain())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/gaspadar-standart-850x850.jpg"),reply_markup=webAppKeyboardHaspadar())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/ujut-web-800x800.jpg"),reply_markup=webAppKeyboardUjut())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/hata/hata_oreh-850x850.jpg"),reply_markup=webAppKeyboardHataDach())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/tualet-haz-800x800.jpg"),reply_markup=webAppKeyboardHozjainBlH())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/talet-odnoskatnyj-800x800.jpg"),reply_markup=webAppKeyboardOdnoklasny())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/fantazija/fantasia_morenii-800x800.jpg"),reply_markup=webAppKeyboardFantasy())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/volat/tyalet_volat_kracka-800x800.jpg"),reply_markup=webAppKeyboardVolat())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/skazka-zel-228x228.jpg"),reply_markup=webAppKeyboardSkazka2())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/tyalet_volat-800x800.jpg"),reply_markup=webAppKeyboardVolatColor())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/prostorchik-800x800.jpg"),reply_markup=webAppKeyboardProstor())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/tualet-skazka2-800x800.jpg"),reply_markup=webAppKeyboardSkazka())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/teremok-800x800.jpg"),reply_markup=webAppKeyboardTeremok())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/tualet/dachnyj-tualet-izba-800x800.jpg"),reply_markup=webAppKeyboardIzba())


# Колодцы
    elif message.text == '/command2':

        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/vorot-850x850.jpg"),reply_markup=webAppKeyboardVorot())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/kolodec-bblokhaus-228x228.jpg"),reply_markup=webAppKeyboardHouseKol())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/img_20210822_130508-800x800.png"),reply_markup=webAppKeyboardHouseKolVorot())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/kolodec-800x800.jpg"),reply_markup=webAppKeyboardHouseKolSkazka())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/kolodec-teremok-800x800.jpg"),reply_markup=webAppKeyboardHouseKolTeremok())
        time.sleep(1)
        bot.send_message(message.from_user.id, ("https://beltree.by/image/cache/catalog/beltree/catalog/domikidljakolodca/kolodec-otkrytyj-800x800.jpg"),reply_markup=webAppKeyboardHouseKolClassic())

# Будки для собак
    elif message.text == '/command3':

        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/standart/hozjain_standart-850x850.jpg"),reply_markup=webAppKeyboardHouseDogHoz())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/standart/hozjain_standart-850x850.jpg"),reply_markup=webAppKeyboardHouseDogStandart())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/budka-shk-800x800.jpg"),reply_markup=webAppKeyboardHouseDogSharik())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/rex/rex-800x800.jpg"),reply_markup=webAppKeyboardHouseDogRex())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/terrasa/dog_terrasa-800x800.jpg"),reply_markup=webAppKeyboardHouseDogTerassa())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/aks/aks-web-800x800.jpg"),reply_markup=webAppKeyboardHouseDogAks())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/budka-s-mini-800x800.jpg"),reply_markup=webAppKeyboardHouseDogMinovoler())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/barbos/budka-s-terrasoj-228x228.jpg"),reply_markup=webAppKeyboardHouseDogMuhtar())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/cheviz/chet-web-800x800.jpg"),reply_markup=webAppKeyboardHouseDogCheviz())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/monti/monti-800x800.jpg"),reply_markup=webAppKeyboardHouseDogMonti())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/monti/monti-800x800.jpg"),reply_markup=webAppKeyboardHouseDogCesar())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/monti/monti-800x800.jpg"),reply_markup=webAppKeyboardHouseDogArchi())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/aks/aks-web-800x800.jpg"),reply_markup=webAppKeyboardHouseDogTamburAks())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/budkasobaka/budka-dlja-sobak-ljuks-850x850.jpg"),reply_markup=webAppKeyboardHouseDogTamburLux())

# Домики для кошек
    elif message.text == '/command4':

        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/ulichnyj/bez-pokarskikt-800x800.jpg"),reply_markup=webAppKeyboardHouseCatStreet())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/ulichnyj/bez-pokarskikt-800x800.jpg"),reply_markup=webAppKeyboardHouseCatStreetCl())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/begemot/begemot-cat-800x800.jpg"),reply_markup=webAppKeyboardHouseCatBegemot())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/begemot/begemot-cat-800x800.jpg"),reply_markup=webAppKeyboardHouseCatKorzhik())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/nanozhkah/na-nozhkah-dub-800x800.jpg"),reply_markup=webAppKeyboardHouseCatNozhki())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/kompot/kompot-s-800x800.jpg"),reply_markup=webAppKeyboardHouseCatKompot())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/kompot/kompot-s-800x800.jpg"),reply_markup=webAppKeyboardHouseCatPushok())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/kompot/kompot-s-800x800.jpg"),reply_markup=webAppKeyboardHouseCatTreuhol())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/kot-barsik-850x850.jpg"),reply_markup=webAppKeyboardHouseCatBarsik())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/villa-228x228.jpg"),reply_markup=webAppKeyboardHouseCatVilla())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/2h-etazhnyj-800x800.jpg"),reply_markup=webAppKeyboardHouseCat2Level())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/tom/tom-web-800x800.jpg"),reply_markup=webAppKeyboardHouseCatTom())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/kottedzh/cattedj-800x800.jpg"),reply_markup=webAppKeyboardHouseCotTaghe())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/gera/gera-web-800x800.jpg"),reply_markup=webAppKeyboardHouseCatHera())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/pethaus/pethaus-800x800.jpg"),reply_markup=webAppKeyboardHouseCatPethaus())
        time.sleep(1)
        bot.send_message(message.from_user.id, ("https://beltree.by/image/cache/catalog/beltree/catalog/bydkikot/pethaus/pethaus-800x800.jpg"),reply_markup=webAppKeyboardHouseCatSkandi())
# Летний душ
    elif message.text == '/command5':
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/dushevye/ujut-800x800.jpg"),reply_markup=webAppKeyboardDushUjut())
# Дровница
    elif message.text == '/command6':
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/drovnicy/piramida/drovnik_piramida-800x800.jpg"),reply_markup=webAppKeyboardDrovnicaPiramida())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/drovnicy/standart/standrt-800x800.jpg"),reply_markup=webAppKeyboardDrovnicaStandart())
        time.sleep(1)
        bot.send_message(message.from_user.id,("https://beltree.by/image/cache/catalog/beltree/catalog/drovnicy/drovnica-800x800.jpg"),reply_markup=webAppKeyboardDrovnicaHozblok())







    else:
        exit()
# # Летние души для дачи
# # Дровницы
# # Детские игровые комплексы
# # Садовый декор
# # Садовая мебель

# 5687768813:AAF6bvd3i8nad6eT9Hx2rLf0gOGCURnRoGY


bot.polling(none_stop=True,interval=0)