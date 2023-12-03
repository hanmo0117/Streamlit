
import streamlit as st
from datetime import datetime as dt
from zhdate import ZhDate
import nums_from_string as nfs
import math
from interval import Interval
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup as bs

st.title('演算法人生')

st.header('介紹')
st.text('這是一個占卜未來的程式 #測試版 1.0.4\n建議用chrome開啟\n姓和名都是最多2字')

st.header('占卜')

last_name = st.text_input('請輸入您的姓')
first_name = st.text_input('請輸入您的名')
birthday_date = st.date_input("請問您的生日是？", None, dt(1900, 1, 1), dt.today())
birthday_time = st.time_input('還有出生時的時間？')

Celestial_Stems = ["癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"] #天干
Terrestrial_Branches = ["亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"] #地支
Five_Elements = ['木', '火', '土', '金', '水'] #五行
Color = ['綠', '紅、 紫', '黃、 咖啡', '白、 金', '藍、 黑']
Number = ['3、 4', '9', '2、 5、 8', '6、 7', '0、 1']
Five_Numbers = ['五格數理',
                "屬木，大吉。宇宙起源，天地開泰太極首領數。",
                "屬木，凶。混飩未定，分離破敗數。",
                "屬火，大吉。進取如意的增進繁榮數。",
                "屬火，凶。破敗凶變的萬事休止數。",
                "屬土，大吉。福祿長壽的福德集門數。",
                "屬土，吉。安穩餘慶吉人天相數。",
                "屬金，吉。剛毅果斷勇往直前的進取數。",
                "屬金，吉。意志剛健的勤勉發展數。",
                "屬水，大凶。興盡凶始，窮乏困苦數。",
                "屬水，大凶。萬事終局充滿損耗數。",
                "屬木，大吉。穩健吉右富貴榮達數。",
                "屬木，凶。意志薄弱的家庭寂寞數。",
                "屬火，大吉。智略超群的博學多才數。",
                "屬火，大凶。淪落天涯失意煩悶數。",
                "屬土，大吉。福壽雙全的立身興家數。",
                "屬土，大吉。貴人相助興家興業的大吉數。",
                "屬金，吉。突破萬難的剛柔兼備數。",
                "屬金，吉。有志竟成的內名有運數。",
                "屬水，大凶。風雲蔽月之災苦重來數。",
                "屬水，大凶。非業破運之災禍不安數。",
                "屬木，大吉。忌女 明月光照，獨立權威數。",
                "屬木，凶。秋草逢霜的兩士相爭數。",
                "屬火，大吉。忌女 旭日東升的質實剛堅數。",
                "屬火，大吉。家門余慶的金錢豐盈數。",
                "屬土，吉。英俊剛毅資性聰敏數。",
                "屬土，凶多於吉。變怪奇異的豪俠數。",
                "屬金，吉多於凶。足智多謀，先苦後甜數。",
                "屬金，大凶。家親緣薄，離群獨處無定數。",
                "屬水，大吉。忌女 智謀兼備，欲望難足數。",
                "屬水，吉多於凶。一成一敗，絕處逢生數。",
                "屬木，大吉。智勇得志，心想事成數。",
                "屬木，吉。權貴顯達的意外惠澤數。",
                "屬火，大吉。忌女 家門隆昌的才德開展數。",
                "屬火，大凶。破家亡身財命危險數。",
                "屬土，吉。溫和平靜的優雅發展數。",
                "屬土，凶。風浪不息的俠義薄運數。",
                "屬金，吉。權威顯達、吉人天相數。",
                "屬金，吉。磨鐵成針刻意經營數。",
                "屬水，大吉。忌女 富貴榮華的變化無窮數。",
                "屬水，吉多於凶。謹慎保安的豪膽邁進數。",
                "屬木，大吉。德高望重的事事如意數。",
                "屬木，吉多於凶。寒嬋在柳，十藝不成數。",
                "屬火，凶多於吉。邪途散財，外祥內苦數。",
                "屬火，大凶。須眉難展力量有限數。",
                "屬土，吉。順風揚帆、新生泰和的萬事如意數。",
                "屬土，大凶。羅網系身離祖成家數。",
                "屬金，大吉。點鐵成金，開花結果的權威進取數。",
                "屬金，大吉。青松方鶴、德智兼備的出身清貴數。",
                "屬水，吉多於凶。吉凶難分的不斷辛勞數。",
                "屬水，吉多於凶。小舟入海，吉凶參半，須防傾覆數。",
                "屬木，吉多於凶。盛衰交加的竭力經營數。",
                "屬木，大吉。先見之明，理想實現數。",
                "屬火，吉多於凶。憂愁困苦，先苦後甜數。",
                "屬火，大凶。多難悲運的難望成功數。",
                "屬土，凶多於吉。外祥內苦的和順不實數。",
                "屬土，大凶。浪裡行舟、歷盡艱辛，四周障害數。",
                "屬金，吉。寒雪青松的最大榮運數。",
                "屬金，吉。晚行遇月、先苦後甘，寬宏揚名數。",
                "屬水，大凶。寒嬋悲風、時運不濟數。",
                "屬水，大凶。爭名奪利，黑暗無光數。",
                "屬木，大吉。名利雙收的修煉積德數。",
                "屬木，大凶。基礎虛弱的艱難困苦數。",
                "屬火，大吉。富貴榮華的身心安泰數。",
                "屬火，大凶。骨肉分離，孤兒悲愁數。",
                "屬土，吉。富貴長壽的光明正大數。",
                "屬土，大凶。內外不和的多欲失福數。",
                "屬金，大吉。財路亨通的志氣堅強數。",
                "屬金，大吉。興家立業的寬容好運數。",
                "屬水，大凶。坐立不安的外世多難數。",
                "屬水，大凶。家運衰退的晚景淒涼數。",
                "屬木，吉多於凶。毫無實質的耗神而勞數。",
                "屬木，凶多於吉。先甜後苦的萬難艱辛數。",
                "屬火，吉。志高力微的努力奮鬥數。",
                "屬火，大凶。沉淪逆境的秋葉落寞數。",
                "屬土，吉多於凶。守者可安，發跡甚遲數。",
                "屬土，大凶。傾覆離散，雖勞無功數。",
                "屬金，吉多於凶。家庭有悅的半吉半凶數。",
                "屬金，吉多於凶。晚境淒涼的功德光榮數。",
                "屬水，大凶。挽回乏力的身疲力盡數。",
                "屬水，大凶。凶星入度的清本縮小數。",
                "屬木，大吉。萬物回春，還原復始的積極盛大數。"]

name = last_name + first_name
birthday_year = birthday_date.year
birthday_month =birthday_date.month
birthday_day =birthday_date.day
birthday = dt(birthday_year, birthday_month, birthday_day)
birthday_lunar = ZhDate.from_datetime(birthday) #農曆XXXX年OX月OX日 not str
lunar_month = nfs.get_nums(str(birthday_lunar))[1] #取農曆'月'
birthday_time_hour = birthday_time.hour + birthday_time.minute/60

if birthday_time_hour in Interval(23, 24, upper_closed = False) or birthday_time_hour in Interval(0, 1, upper_closed = False):
    birthday_time_TB = "子"
elif birthday_time_hour in Interval(1, 3, upper_closed = False):
    birthday_time_TB = "丑"
elif birthday_time_hour in Interval(3, 5, upper_closed = False):
    birthday_time_TB = "寅"
elif birthday_time_hour in Interval(5, 7, upper_closed=False):
    birthday_time_TB = "卯"
elif birthday_time_hour in Interval(7, 9, upper_closed=False):
    birthday_time_TB = "辰"
elif birthday_time_hour in Interval(9, 11, upper_closed = False):
    birthday_time_TB = "巳"
elif birthday_time_hour in Interval(11, 13, upper_closed = False):
    birthday_time_TB = "午"
elif birthday_time_hour in Interval(13, 15, upper_closed = False):
    birthday_time_TB = "未"
elif birthday_time_hour in Interval(15, 17, upper_closed = False):
    birthday_time_TB = "申"
elif birthday_time_hour in Interval(17, 19, upper_closed = False):
    birthday_time_TB = "酉"
elif birthday_time_hour in Interval(19, 21, upper_closed = False):
    birthday_time_TB = "戌"
elif birthday_time_hour in Interval(21, 23, upper_closed = False):
    birthday_time_TB = "亥"

A = Celestial_Stems[(birthday_year - 3) % 10]
B = Terrestrial_Branches[(birthday_year - 3) % 12]
C = Celestial_Stems[(Celestial_Stems.index(A, 1, 11) * 2 + lunar_month)%10]
D = Terrestrial_Branches[lunar_month + 2]
E = Celestial_Stems[(((birthday_year - 1) * 5 + math.floor((birthday_year - 1) / 4) + int(birthday.strftime('%j'))) % 60) % 10]
F = Terrestrial_Branches[(((birthday_year - 1) * 5 + math.floor((birthday_year - 1) / 4) + int(birthday.strftime('%j'))) % 60) % 12]
H = birthday_time_TB
G = Celestial_Stems[(Celestial_Stems.index(E, 1, 11) * 2 - 2 + Terrestrial_Branches.index(H, 1, 13)) % 10]

Table_1 = pd.DataFrame({'年柱': [A, B], '月柱': [C, D], '日柱': [E, F], '時柱': [G, H]}, index = ['天干', '地支'])

A_Five_Elements = A.translate(str.maketrans('甲乙丙丁戊己庚辛壬癸', '木木火火土土金金水水'))
B_Five_Elements = B.translate(str.maketrans('子丑寅卯辰巳午未申酉戌亥', '水土木木土火火土金金土水'))
C_Five_Elements = C.translate(str.maketrans('甲乙丙丁戊己庚辛壬癸', '木木火火土土金金水水'))
D_Five_Elements = D.translate(str.maketrans('子丑寅卯辰巳午未申酉戌亥', '水土木木土火火土金金土水'))
E_Five_Elements = E.translate(str.maketrans('甲乙丙丁戊己庚辛壬癸', '木木火火土土金金水水'))
F_Five_Elements = F.translate(str.maketrans('子丑寅卯辰巳午未申酉戌亥', '水土木木土火火土金金土水'))
G_Five_Elements = G.translate(str.maketrans('甲乙丙丁戊己庚辛壬癸', '木木火火土土金金水水'))
H_Five_Elements = H.translate(str.maketrans('子丑寅卯辰巳午未申酉戌亥', '水土木木土火火土金金土水'))
Five_Elements_total = [A_Five_Elements, B_Five_Elements, C_Five_Elements, D_Five_Elements, E_Five_Elements, F_Five_Elements, G_Five_Elements, H_Five_Elements]
Five_Elements_Counts = [Five_Elements_total.count('木'), Five_Elements_total.count('火'), Five_Elements_total.count('土'), Five_Elements_total.count('金'), Five_Elements_total.count('水')]
The_Least_Element = [Five_Elements[i] for i, j in enumerate(Five_Elements_Counts) if j == 0]
The_Most_Element = [Five_Elements[i] for i, j in enumerate(Five_Elements_Counts) if j == max(Five_Elements_Counts)]
if len(The_Least_Element) == 0:
    The_Least_Element = '無'
if len(The_Most_Element) > 2:
    The_Most_Element = '無'

Lucky_Color = [Color[i] for i, j in enumerate(Five_Elements_Counts) if j == 0]
Lucky_Number = [Number[i] for i, j in enumerate(Five_Elements_Counts) if j == 0]
if len(Lucky_Color) == 0:
    Lucky_Color = '無'
if len(Lucky_Number) == 0:
    Lucky_Number = '無'

age = dt.today().year - birthday_year - ((dt.today().month, dt.today().day) < (birthday_month, birthday_day))

if st.button('占卜結果'):
    try:
        st.table(Table_1)

        texts = bs(requests.get(url = f"https://kangxizidian.com/search/index.php?stype=Word&sword={name}&detail=n").text)('td', align = "center", valign = "top")
        Strokes = list(map(lambda x: texts[x].text.replace('\n', '')[texts[x].text.find(':') + 10: texts[x].text.find('畫')].replace('畫', ''), list(range(1, len(name) + 1))))
        Last_Name_Strokes = list(map(int, list(map(lambda x: Strokes[x], list(range(0, len(last_name)))))))
        First_Name_Strokes = list(map(int, list(map(lambda x: Strokes[x], list(range(len(last_name), len(name)))))))
        if len(last_name) == 1:  # 天格
            Tiange = Last_Name_Strokes[0] + 1
        elif len(last_name) == 2:
            Tiange = Last_Name_Strokes[0] + Last_Name_Strokes[1]
        if len(last_name) == 1:  # 人格
            Renge = First_Name_Strokes[0] + Last_Name_Strokes[0]
        elif len(last_name) == 2:
            Renge = First_Name_Strokes[1] + Last_Name_Strokes[0]
        if len(first_name) == 1:  # 地格
            Dige = First_Name_Strokes[0] + 1
        elif len(first_name) == 2:
            Dige = First_Name_Strokes[0] + First_Name_Strokes[1]
        Zonge = sum(Last_Name_Strokes) + sum(First_Name_Strokes)  # 總格
        Waige = Tiange + Dige - Renge  # 外格

        Table_2 = pd.DataFrame({'解釋': [Five_Numbers[Tiange], Five_Numbers[Renge], Five_Numbers[Dige], Five_Numbers[Zonge],  Five_Numbers[Waige]]}, index = ['天格', '人格', '地格', '總格', '外格'])

        st.table(Table_2)
        st.write(f'命格五行：{E}')
        st.write(f'五行欠缺：{"、 ".join(The_Least_Element)}')
        st.write(f'五行過旺：{"、 ".join(The_Most_Element)}')
        st.write(f'Lucky color：{"、 ".join(Lucky_Color)}')
        st.write(f'Lucky number：{"、 ".join(Lucky_Number)}')
        st.write('')
        if age in Interval(0, 12):
            st.write('您現在的流年：')
            st.write( f'天格：{Five_Numbers[Tiange]}')
            st.write( f'地格：{Five_Numbers[Dige]}')
        elif age in Interval(13, 24):
            st.write('您現在的流年：')
            st.write(f'人格：{Five_Numbers[Renge]}')
            st.write(f'地格：{Five_Numbers[Dige]}')
        elif age in Interval(25, 36):
            st.write('您現在的流年：')
            st.write(f'人格：{Five_Numbers[Renge]}')
            st.write (f'外格：{Five_Numbers[Waige]}')
        elif age in Interval(37, 48):
            st.write('您現在的流年：' )
            st.write(f'天格：{Five_Numbers[Tiange]}')
            st.write(f'人格：{Five_Numbers[Renge]}')
        elif age in Interval(48, float('inf')):
            st.write('您現在的流年：')
            st.write(f'總格：{Five_Numbers[Zonge]}')
        st.write('')
        st.success('占卜完成！')
        st.write('')
    except:
        st.error('您輸入的姓名可能有誤或不支援，請確認！')

st.text('如果有任何問題，請聯絡b10203037@ntu.edu.tw\nHan Mo\n'
        '程式碼：https://github.com/hanmo0117/Streamlit/blob/main/FortuneTellingAlgorithm/main.py\n'
        'APP：https://hanmo0117-streamlit--main-mpbokl.streamlit.app/')
