from base_tag import *
from xml_string_builder import XmlStringBuilder

class XmlStringParser:
    def parse(self, data):
        if not data:
            raise Exception('Empty parse data')
        tag_list = []
        tag_data = ''
        open_tag_complete = False
        for index, symbol in enumerate(data, 0):
            if symbol == BEGIN_TAG:
                #if data[index+1] == '/':
                 #   open_tag_complete = False
                if open_tag_complete:
                    tag_data.strip()
                    tag_list.append(tag_data)
                    tag_data = ''
                    open_tag_complete = False
                tag_data += symbol
                continue
            elif symbol == END_TAG:
                tag_data += symbol
                open_tag_complete = True
                continue
            elif symbol not in ["\n", "\r"]:
                tag_data += symbol
        if tag_data.startswith('<') and tag_data.endswith('>'):
            tag_list.append(tag_data)
        print(tag_list)
        return tag_list

test = """<note>
<test>
<to>Вася</to>
</test>
<from>Света</from>
<heading>Напоминание</heading>
<body>Позвони мне завтра!</body>
</note>"""

test2 = """
<breakfast_menu>
<food>
<name>Бельгийские Вафли</name>
<price>$5.95</price>
<description>две известных Бельгийских Вафли с обилием настоящего кленового сиропа</description>
<calories>650</calories>
</food>
<food>
<name>Бельгийские Вафли с Земляникой</name>
<price>$7.95</price>
<description>легкие Бельгийские вафли с земляникой, покрытые взбитыми сливками</description>
<calories>900</calories>
</food>
<food>
<name>Бельгийские Вафли с Ягодами</name>
<price>$8.95</price>
<description>легкие Бельгийские вафли с различными свежими ягодами, покрытые взбитыми сливками</description>
<calories>900</calories>
</food>
<food>
<name>Французский Тост</name>
<price>$4.50</price>
<description>толстые куски, сделанные из кусочков домашнего хлеба из опары</description>
<calories>600</calories>
</food>
<food>
<name>Домашний Завтрак</name>
<price>$6.95</price>
<description>пара яиц, бекон или колбаса, тост, и наши всегда популярные картофельные оладьи</description>
<calories>950</calories>
</food>
</breakfast_menu>
"""
test3 = """
<CATALOG>
<CD>
<TITLE>Имперская Пародия</TITLE>
<ARTIST>Боб Дилан</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Колумбия</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Спрячь свое сердце</TITLE>
<ARTIST>Бонни Тайлер</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Записи си-би-эс</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1988</YEAR>
</CD>
<CD>
<TITLE>Лучшие Хиты</TITLE>
<ARTIST>Долли Партон</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Ар-Си-Эй</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1982</YEAR>
</CD>
<CD>
<TITLE>Still got the blues</TITLE>
<ARTIST>Гарри Мур</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Virgin records</COMPANY>
<PRICE>10.20</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Эрос</TITLE>
<ARTIST>Эрос Рамазотти</ARTIST>
<COUNTRY>ЕС</COUNTRY>
<COMPANY>BMG</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1997</YEAR>
</CD>
<CD>
<TITLE>Только одну ночь</TITLE>
<ARTIST>Бии Гиис</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Полидор</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1998</YEAR>
</CD>
<CD>
<TITLE>Мама Сильвии</TITLE>
<ARTIST>Доктор Хук</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Си-би-эс</COMPANY>
<PRICE>8.10</PRICE>
<YEAR>1973</YEAR>
</CD>
<CD>
<TITLE>Мэгги Мэй</TITLE>
<ARTIST>Род Стюарт</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Пиквик</COMPANY>
<PRICE>8.50</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Романза</TITLE>
<ARTIST>Андреа Бочелли</ARTIST>
<COUNTRY>ЕС</COUNTRY>
<COMPANY>Полидор</COMPANY>
<PRICE>10.80</PRICE>
<YEAR>1996</YEAR>
</CD>
<CD>
<TITLE>Когда мужчина любит женщину</TITLE>
<ARTIST>Пирси Слидж</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Атлантика</COMPANY>
<PRICE>8.70</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Черный Ангел</TITLE>
<ARTIST>Дикая Роза</ARTIST>
<COUNTRY>ЕС</COUNTRY>
<COMPANY>Мега</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1995</YEAR>
</CD>
<CD>
<TITLE>1999 Номинанты Грэмми</TITLE>
<ARTIST>(несколько)</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Грэмми</COMPANY>
<PRICE>10.20</PRICE>
<YEAR>1999</YEAR>
</CD>
<CD>
<TITLE>Для хороших времен</TITLE>
<ARTIST>Кенни Роджерс</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Mucik Мастер</COMPANY>
<PRICE>8.70</PRICE>
<YEAR>1995</YEAR>
</CD>
<CD>
<TITLE>Стиль Большого Человека</TITLE>
<ARTIST>Уилл Смит</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Колумбия</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1997</YEAR>
</CD>
<CD>
<TITLE>Ниссовый Мед</TITLE>
<ARTIST>Ван Моррисон</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Полидор</COMPANY>
<PRICE>8.20</PRICE>
<YEAR>1971</YEAR>
</CD>
<CD>
<TITLE>Соулсвилл</TITLE>
<ARTIST>Джорн Хоэл</ARTIST>
<COUNTRY>Норвегия</COUNTRY>
<COMPANY>WEA</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1996</YEAR>
</CD>
<CD>
<TITLE>Лучшее из</TITLE>
<ARTIST>Кэт Стивенс</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Исландия</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1990</YEAR>
</CD>
<CD>
<TITLE>Стоп</TITLE>
<ARTIST>Сэм Браун</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>А и М</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1988</YEAR>
</CD>
<CD>
<TITLE>Мост Шпионов</TITLE>
<ARTIST>T'Pau</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Сирена</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Приватный Танцор</TITLE>
<ARTIST>Тина Тернер</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Капитолий</COMPANY>
<PRICE>8.90</PRICE>
<YEAR>1983</YEAR>
</CD>
<CD>
<TITLE>Midt om natten</TITLE>
<ARTIST>Ким Ларсен</ARTIST>
<COUNTRY>ЕС</COUNTRY>
<COMPANY>Смесь</COMPANY>
<PRICE>7.80</PRICE>
<YEAR>1983</YEAR>
</CD>
<CD>
<TITLE>Паваротти Гала Концерт</TITLE>
<ARTIST>Лучиано Паваротти</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>ДЕККА</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1991</YEAR>
</CD>
<CD>
<TITLE>Док в заливе</TITLE>
<ARTIST>Отис Реддинг</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>Атлантика</COMPANY>
<PRICE>7.90</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Книга с картинками</TITLE>
<ARTIST>Симпли Рэд</ARTIST>
<COUNTRY>ЕС</COUNTRY>
<COMPANY>Электра</COMPANY>
<PRICE>7.20</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Красный</TITLE>
<ARTIST>Коммунары</ARTIST>
<COUNTRY>Соединенное Королевство</COUNTRY>
<COMPANY>Лондон</COMPANY>
<PRICE>7.80</PRICE>
<YEAR>1987</YEAR>
</CD>
<CD>
<TITLE>Освободи мое сердце</TITLE>
<ARTIST>Джо Коккер</ARTIST>
<COUNTRY>США</COUNTRY>
<COMPANY>EMI</COMPANY>
<PRICE>8.20</PRICE>
<YEAR>1987</YEAR>
</CD>
</CATALOG>
"""
test4 = """
<messages>
<note id="p501">
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
  <test id=55 temp=44/>
</note>

<note id="p502">
  <to>Jani</to>
  <from>Tove</from>
  <heading>Re: Reminder</heading>
  <body>I will not!</body>
</note>
</messages>"""

t = XmlStringParser().parse(test)

z = XmlStringBuilder().build_tags(t)