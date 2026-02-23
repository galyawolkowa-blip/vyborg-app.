from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', '0')

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.fitimage import FitImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
import os

# ----- Путь к папке с изображениями (относительно main.py) -----
BASE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'data')

class RoundButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(40), dp(40))
        self.color = (1, 1, 1, 1)
        self.font_size = dp(18)
        self.bold = True
        self.halign = 'center'
        self.valign = 'middle'

        with self.canvas.before:
            Color(0.333, 0.694, 0.557, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(22),]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# ----- Данные о достопримечательностях (исправлены имена файлов) -----
LANDMARKS = [
    {
        "id": 1, "name": "ВЫБОРГСКИЙ ЗАМОК", "pos_x": 0.39, "pos_y": 0.42,
        "history": "Выборгский замок был основан шведами в 1293 году как форпост на Карельском перешейке. За свою более чем семивековую историю замок неоднократно переходил из рук в руки, отражая сложную военную историю региона. В 1710 году войска Петра I взяли замок, после чего он вошёл в состав Российской империи. В XX веке замок стал ареной советско-финских военных конфликтов. Сегодня это единственный в России полностью сохранившийся памятник западноевропейского средневекового военного зодчества. В замке располагается музей, где представлены экспозиции по истории города и края, а также проводятся рыцарские турниры и исторические реконструкции.",
        "quotes": [
            "«На островке, возвышаясь веками,\nСтарая крепость на страже стоит.\nЗамок, пленённый морскими ветрами,\nДревние тайны безмолвно хранит.»\n— Песня о Выборге (М. и В. Унуковские)",
            "«И с высоты в прошлом грозного форта\nВижу я город прекрасный вдали.\nОн как фрегат продвигается гордо\nНа волнах истории славной земли.»\n— Песня о Выборге (М. и В. Унуковские)",
                    "У ВЫБОРГСКОГО ЗАМКА\n\nУ древних скал, у этих берегов\nКто мне ответит коротко, спроси я:\nГде силы ты брала, моя Россия,\nКак одолела всех твоих врагов?\nЗдесь шведские прямые паруса\nКак призраки, белели над водою,\nИ веяло от Балтики бедою\nЧужие раздавались голоса.\nЗдесь ставили на якорь корабли\nНепрошенные гости славянина,\nНа смертный бой благословляя сына,\nМать голову склоняла до земли.\nЛевонский хлыст, немецкая узда\nИ шведские оковы — все неволя...\nЧернело незасеянное поле,\nПустели и нищали города.\nНо тень неукротимого Петра\nМне видится на палубе фрегата.\nИ пушечные ядра, как расплата,\nУдарили по крепости с утра.\nОсада, приступ — ратная страда,\nНелегкая солдатская работа,\nРубахи, побелевшие от пота,\nОт крови потемневшая вода.\nЗаконы чести зная наизусть,\nКлялись царю и воинскому стягу.\nИ помнили солдатскую присягу,\nИ умирали за святую Русь.\n\n— Иван Удовик",
                    "НА ВЫБОРГ!\n\nНа Выборг!\n       Танки били с ходу.\n– Комбриг,\n        ты только прикажи –\nПрошли огонь,\n       завалы, воду, –\nПройдем и эти рубежи!\nДугою выгнулись пролеты,\nХодили сваи ходуном.\n– Не торопись в огонь,\n        пехота, –\nПроходы пушками пробьем!\n– Победа будет\n       нам наградой,\nНаградой высшей,\n       сразу всем!–\nШутил комбриг,\n      кумир бригады\nВ своих неполных\n       двадцать семь.\nВ огне дома,\n      взрывались мины,\nИ в пыль –\n      бетон и кирпичи...\nШли танки –\n       грозные машины.\nДаешь от Выборга ключи!\n\n— Иван Удовик, 1995",
            ],
        "color": "#3F8067",
        "image": "cathedral.jpeg"
    },
    {
        "id": 2, "name": "ПАРК МОНРЕПО", "pos_x": 0.29, "pos_y": 0.81,
        "history": "Парк Монрепо — уникальный скальный пейзажный парк, расположенный на берегу Выборгского залива. Его создание началось в конце XVIII века, когда эти земли принадлежали коменданту Выборгской крепости Петру Ступишину. Название парка переводится с французского как 'мой отдых'. Особую ценность представляют скальные ландшафты, деревянная архитектура в стиле неоготики, а также система прудов и каналов. В парке расположены памятники архитектуры: усадебный дом, библиотечный флигель, китайские мостики и капелла Людвигсбург. Парк сильно пострадал во время войн XX века, но в настоящее время ведутся работы по его восстановления.",
        "quotes": [
            "«Парк Монрепо – обаяние рая,\nСветлый приют для души, благодать.\nТайны неспешно свои открывая,\nСоздан сердца он людей восхищать.»\n— Песня о Выборге (М. и В. Унуковские)",
            "«Чтобы понять и почувствовать романтическую поэзию и эстетику XVIII–XIX вв., пожалуй, лучшее место сложно найти.»\n— Варвара Каширина, 'Романтическая поэма в камне'",
                    "В ГРАНИТЕ ВИЖУ ЛИК ВОЙНЫ\n\nПротивотанковые надолбы...\nУдар последний по врагу.\nНе вспоминать о вас\n            мне надо бы,\nА я забыть вас не могу.\nВ граните вижу лик войны,\nС краями острыми и\n          рваными.\nНезаживающими ранами\nЛеса Карелии полны.\nНа час – обстрел,\n            на век – следы.\nЗдесь сосны падали, которые\nДва века жили, меднокорые\nНе зная огненной беды.\nЯ под сосною постою.\nДеревья ввысь уходят\n           кронами.\nИ молодыми, и зелеными\nВы были в памятном бою.\nКак далеко они видны,\nСтволы с осколочными\n           ранами.\nСтоят деревья ветеранами\nНезабываемой войны.\n\n— Иван Удовик",
                            "Серое небо и серое море\nСквозь золотых и пурпурных листов,\nСловно тяжелое старое горе\nСмолкла в последнем прощальном уборе\nСветлых, прозрачных и радужных снов.\n\n— Владимир Соловьёв, «Монрепо», 1894",
        ],
        "color": "#3F8067",
        "image": "castle.jpg"
    },
    {
        "id": 3, "name": "БАШНЯ РАТУШИ", "pos_x": 0.51, "pos_y": 0.25,
        "history": "Башня Ратуши — одна из немногих сохранившихся боевых башен Выборгской крепостной стены, построенной в 1470-х годах. Название башни происходит от расположенной рядом ратуши. Изначально башня была пятиэтажной и венчалась высокой кровлей. В XVII веке, когда город расширился и крепостные стены утратили оборонное значение, башня использовалась как колокольня доминиканского собора, а затем как складское помещение. В 1960-х годах башня была отреставрирована и сегодня в ней размещается экспозиция, рассказывающая о средневековом Выборге и истории крепостных сооружений города.",
        "quotes": [
            "«Город церквей, площадей, фестиваля\nВыборг радушно встречает друзей\nГород-легенда и край Калевалы\nГород под небом открытый музей.»\n— Песня о Выборге (М. и В. Унуковские)",
                "МОЙ ГОРОД\n\nТы дорог мне, мой город древний,\nНу что поделаешь – люблю,\nС горы гранитной Батарейной\nЛюбуюсь на красу твою.\n\nИ в сердце встрепенется что-то,\nКогда стою, смотрю без слов,\nКак будто с птичьего полёта,\nНа ожерелье островов.\n\nЗдесь крепость высится атлантом,\nВзвалив на плечи облака,\nВолна серебряным накатом\nЛаскает тихо берега.\n\nПодобно чайкам быстрокрылым\nЛетят по ветру паруса,\nИ парк над солнечным заливом\nНам дарит птичьи голоса.\n\nЛюблю тебя и в зимах длинных,\nИ в дымке летних светлых дней.\nНа самых солнечных и дивных\nНе променяю – хоть убей!\n\nФорпост родной моей отчизны,\nГоржусь я доблестью твоей.\nКрасуйся, Выборг, ради жизни\nИ светлых, добрых мирных дней.\n\n— Адольф Асаев, 2004",    
        ],
        "color": "#3F8067",
        "image": "ratusha.jpg"
    },
    {
        "id": 4, "name": "УСАДЬБА БЮРГЕРА", "pos_x": 0.58, "pos_y": 0.30,
        "history": "Усадьба бюргера — единственный в Выборге полностью сохранившийся жилой дом шведского времени, построенный в XVI-XVII веках. Этот каменный дом типичен для архитектуры средневекового Выборга: первый этаж использовался как мастерская или торговая лавка, второй этаж был жилым. В XX веке дом был отреставрирован, и сегодня в нём размещается музей, воссоздающий атмосферу жизни выборгского бюргера. Здесь можно увидеть интерьеры XVII-XVIII веков, предметы быта, ремесленные инструменты. Во дворе усадьбы находится колодец и небольшой садик, характерные для средневековых городских усадеб.",
        "quotes": [
            "«Средь улиц твоих незнакомых брожу.\nДобрость заливом, под ветром дрожу.\nИ встречные лица пытливо листаю,\nКак новую книгу, запоем читаю!»\n— О. Долматов"
        ],
        "color": "#3F8067",
        "image": "burger.png"
    },
    {
        "id": 5, "name": "ЧАСОВАЯ БАШНЯ", "pos_x": 0.46, "pos_y": 0.33,
        "history": "Часовая башня — бывшая колокольня разрушенного в советско-финских войнах кафедрального собора Выборга. Строительство башни началось в XV веке, а в 1753 году на ней были установлены часы с колоколом, подаренные императрицей Екатериной II. В 1796 году башня получила третий ярус в стиле классицизма. Высота башни составляет 25 метров. Часовой механизм исправно работал до 1940-х годов. Во время войны башня сильно пострадала, но была восстановлена в послевоенные годы. Сегодня это одна из архитектурных доминант Старого города, с которой открывается прекрасный вид на исторический центр Выборга.",
        "quotes": [
            "«Часовня на скале, как страж столетий,\nХранит покой ушедших поколений.\nИ колокольный звон, что смолк в войну,\nДоносит до нас прошлого весну.»\n— Из архивных материалов",
                    "МЕЛОДИЯ ВЫБОРГА\n\nЕдва утихнет гул цивилизаций,\nМелодия над Выборгом плывёт\nРекою льющихся импровизаций,\nЗвучанием Небес нежнейших нот.\n\nПритихло всё, чтоб музыки парящей\nУслышать можно было каждый такт.\nСлияния былого с настоящим\nСвершается неповторимый акт.\n\nИ счастлив тот, чьё ухо уловило\nНезримых инструментов унисон,\nНад городом вечерним, над заливом\nПод тихие аплодисменты волн.\n\n— Светлана Дзюдзе, 2019",
        ],
        "color": "#3F8067",
        "image": "clock_tower.jpg"
    },
    {
        "id": 6, "name": "КРУГЛАЯ БАШНЯ", "pos_x": 0.60, "pos_y": 0.37,
        "history": "Круглая башня — мощное артиллерийское укрепление, построенное в 1547-1550 годах по приказу шведского короля Густава Васы. Башня диаметром 21 метр и толщиной стен до 4 метров входила в систему городских укреплений. В XVII веке, после перестройки городских укреплений, башня утратила военное значение и использовалась как склад, а затем как тюрьма. В 1920-х годах башню реконструировали под ресторан по проекту архитектора Уно Ульберга. Сегодня в Круглой башне располагается ресторан, а также проводятся культурные мероприятия. Башня является одним из символов Выборга и прекрасным образцом фортификационного искусства XVI века.",
        "quotes": [
            "«Под куполом её шелома разверзнуты глаза бойниц...\nПри виде сей картины странной,\nты поймёшь, в каком ты городе живёшь!»\n— 'Баллада о древнем Выборге'",
                    "В ВЫБОРГЕ\n\nОгромная подводная ступень,\nВедущая в Нептуновы владенья, —\nТам стынет Скандинавия, как тень,\nВся — в ослепительном одном виденье.\nБезмолвна песня — музыка нема,\nНо воздух жжется их благоуханьем,\nИ на коленях белая зима\nСледит за всем с молитвенным вниманьем.\n\nЗемля хотя и не родная,\nНо памятная навсегда,\nИ в море нежно-ледяная\nИ несоленая вода.\nНа дне песок белее мела,\nА воздух пьяный, как вино,\nИ сосен розовое тело\nВ закатный час обнажено.\nА сам закат в волнах эфира\nТакой, что мне не разобрать,\nКонец ли дня, конец ли мира,\nИль тайна тайн во мне опять.\n\n— О.А. Ладыженская, 1964",
        ],
        "color": "#3F8067",
        "image": "round_tower.jpg"
    },
    {
        "id": 7, "name": "БИБЛИОТЕКА ААЛТО", "pos_x": 0.80, "pos_y": 0.23,
        "history": "Библиотека Алвара Аалто — выдающийся памятник архитектуры функционализма, построенный в 1933-1935 годах по проекту знаменитого финского архитектора Алвара Аалто. Здание считается одним из лучших произведений Аалто и эталоном библиотечной архитектуры. Особенностями библиотеки являются волнообразный потолок лекционного зала, обеспечивающий идеальную акустику, и система верхнего освещения через специальные световые фонари. Во время войны здание сильно пострадало, но было восстановлено в 1950-х годах. Сегодня это центральная городская библиотека, которая продолжает использоваться по своему прямому назначению, оставаясь важным культурным центром Выборга.",
        "quotes": [
            "«…Вся — в ослепительном одном виденье.\nВся — в ослепительном одном виденье.\nИ на коленях белая зима.\nСледят за всем с молитвенным вниманием.»\n— 'Выборгский коммунист', 24.09.1964"
        ],
        "color": "#3F8067",
        "image": "library.png"
    }
]

# ----- Экраны приложения (без изменений, кроме заголовка) -----
class MapScreen(MDScreen):
    def on_enter(self):
        self.clear_widgets()
        self.build_interface()

    def build_interface(self):
        # Фоновая карта
        map_path = os.path.join(BASE_IMAGE_PATH, "vyborg_map.png")
        if os.path.exists(map_path):
            map_image = FitImage(source=map_path, size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
            self.add_widget(map_image)

        # Заголовок (изменён на "литВЫБОРГ")
        title_box = MDBoxLayout(
            orientation='vertical',
            size_hint=(1, 0.15),
            pos_hint={'top': 1},
            padding=[20, dp(38), 20, 10],
            spacing=5
        )

        title = MDLabel(
            text="литВЫБОРГ",  # новое название
            halign="center",
            theme_text_color="Custom",
            text_color=(0.20, 0.10, 0.06, 20),
            font_style="H5",
            bold=True
        )

        subtitle = MDLabel(
            text="Проект Волковой Галины · 10 класс",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.42, 0.35, 0.24, 1),
            font_style="Subtitle2"
        )

        title_box.add_widget(title)
        title_box.add_widget(subtitle)

        # Кнопки достопримечательностей
        for landmark in LANDMARKS:
            btn = RoundButton(
                text=str(landmark["id"]),
                pos_hint={"center_x": landmark["pos_x"], "center_y": landmark["pos_y"]}
            )
            btn.bind(on_release=lambda instance, l=landmark: self.show_landmark(l))
            self.add_widget(btn)

        # Нижняя панель
        control_box = MDBoxLayout(
            orientation='horizontal',
            size_hint=(0.9, 0.09),
            pos_hint={'center_x': 0.5278, 'y': 0.07},
            spacing=20
        )

        buttons = [
            ("МАРШРУТЫ", "routes", "#8988CF"),
            ("ДНЕВНИК", "diary", "#84BBA3"),
            ("О ПРОЕКТЕ", "about", "#A8C3DA")
        ]

        for text, screen, color in buttons:
            btn = MDRaisedButton(
                text=text,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                md_bg_color=color,
                on_release=lambda instance, s=screen: self.go_to_screen(s)
            )
            control_box.add_widget(btn)

        self.add_widget(title_box)
        self.add_widget(control_box)

    def show_landmark(self, landmark):
        app = MDApp.get_running_app()
        app.current_landmark = landmark
        self.manager.current = "landmark"

    def go_to_screen(self, screen_name):
        self.manager.current = screen_name

class LandmarkScreen(MDScreen):
    # ... (код без изменений, но убедитесь, что пути к изображениям формируются правильно)
    def on_enter(self):
        self.build_interface()

    def build_interface(self):
        self.clear_widgets()
        app = MDApp.get_running_app()
        landmark = app.current_landmark
        current_idx = LANDMARKS.index(landmark)

        main_scroll = MDScrollView()
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=15,
            spacing=15,
            size_hint_y=None
        )
        main_layout.bind(minimum_height=main_layout.setter('height'))

        header = MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)

        back_btn = MDRaisedButton(
            text="<<- КАРТА",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#589174",
            size_hint=(0.3, 1),
            on_release=lambda instance: self.go_to_map()
        )

        title_label = MDLabel(
            text=landmark['name'],
            halign="center",
            theme_text_color="Custom",
            text_color=(0.55, 0.76, 0.72, 1),
            font_style="H5",
            bold=True,
            size_hint=(0.7, 1)
        )

        header.add_widget(back_btn)
        header.add_widget(title_label)

        content_card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            padding=0,
            spacing=0,
            elevation=5,
            radius=[20],
            md_bg_color=(1, 1, 1, 1)
        )
        content_card.bind(minimum_height=content_card.setter('height'))

        if landmark.get("image"):
            image_card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height=dp(200),
                padding=0,
                elevation=0,
                radius=[20, 20, 0, 0],
                md_bg_color=(0.9, 0.9, 0.9, 1)
            )

            image_path = os.path.join(BASE_IMAGE_PATH, landmark["image"])
            try:
                if os.path.exists(image_path):
                    print(f"Загружаем изображение: {image_path}")
                    image = FitImage(
                        source=image_path,
                        size_hint_y=None,
                        height=dp(200),
                        radius=[20, 20, 0, 0]
                    )
                    image_card.add_widget(image)
                else:
                    print(f"Файл не найден: {image_path}")
                    placeholder = MDLabel(
                        text=f"Изображение не найдено",
                        halign="center",
                        valign="middle",
                        theme_text_color="Custom",
                        text_color=(0.8, 0.2, 0.2, 1)
                    )
                    image_card.add_widget(placeholder)
            except Exception as e:
                print(f"Ошибка загрузки изображения {landmark['name']}: {e}")
                error_label = MDLabel(
                    text=f"Ошибка загрузки изображения",
                    halign="center",
                    valign="middle",
                    theme_text_color="Custom",
                    text_color=(0.8, 0.2, 0.2, 1)
                )
                image_card.add_widget(error_label)

            content_card.add_widget(image_card)

        text_container = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15,
            size_hint_y=None
        )
        text_container.bind(minimum_height=text_container.setter('height'))

        history_title = MDLabel(
            text="История места:",
            theme_text_color="Custom",
            text_color=(0.3, 0.2, 0.1, 1),
            bold=True,
            size_hint_y=None,
            height=dp(30)
        )

        history_text = MDLabel(
            text=landmark["history"],
            theme_text_color="Custom",
            text_color=(0.4, 0.3, 0.2, 1),
            size_hint_y=None,
            size_hint_x=1,
            text_size=(None, None)
        )
        history_text.bind(texture_size=history_text.setter('size'))

        quotes_title = MDLabel(
            text="Литературные цитаты:",
            theme_text_color="Custom",
            text_color=(0.3, 0.2, 0.1, 1),
            bold=True,
            size_hint_y=None,
            height=dp(30)
        )

        text_container.add_widget(history_title)
        text_container.add_widget(history_text)
        text_container.add_widget(quotes_title)

        for quote in landmark["quotes"]:
            quote_card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                size_hint_x=1,
                padding=15,
                spacing=10,
                elevation=2,
                radius=[12],
                md_bg_color=(0.95, 0.93, 0.88, 1)
            )

            quote_text = MDLabel(
                text=quote,
                theme_text_color="Custom",
                text_color=(0.25, 0.18, 0.1, 1),
                size_hint_y=None,
                size_hint_x=1,
                text_size=(None, None)
            )
            quote_text.bind(texture_size=quote_text.setter('size'))

            quote_card.add_widget(quote_text)
            quote_card.bind(minimum_height=quote_card.setter('height'))
            text_container.add_widget(quote_card)

        content_card.add_widget(text_container)
        content_card.bind(minimum_height=content_card.setter('height'))

        nav_box = MDBoxLayout(
            size_hint=(1, None),
            height=dp(50),
            spacing=20
        )

        prev_btn = MDRaisedButton(
            text="<<- НАЗАД",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#8988CF",
            disabled=current_idx == 0,
            on_release=lambda instance: self.navigate(-1)
        )

        nav_info = MDLabel(
            text=f"Точка {current_idx + 1} из {len(LANDMARKS)}",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.4, 0.3, 0.2, 1)
        )

        next_btn = MDRaisedButton(
            text="ДАЛЕЕ ->>",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#8988CF",
            disabled=current_idx == len(LANDMARKS) - 1,
            on_release=lambda instance: self.navigate(1)
        )

        nav_box.add_widget(prev_btn)
        nav_box.add_widget(nav_info)
        nav_box.add_widget(next_btn)

        main_layout.add_widget(header)
        main_layout.add_widget(content_card)
        main_layout.add_widget(nav_box)

        main_scroll.add_widget(main_layout)
        self.add_widget(main_scroll)

    def go_to_map(self):
        self.manager.current = "map"

    def navigate(self, direction):
        app = MDApp.get_running_app()
        current_idx = LANDMARKS.index(app.current_landmark)
        new_idx = current_idx + direction

        if 0 <= new_idx < len(LANDMARKS):
            app.current_landmark = LANDMARKS[new_idx]
            self.build_interface()

class RoutesScreen(MDScreen):
    # ... (без изменений, только импорты уже есть)
    def on_enter(self):
        self.build_interface()

    def build_interface(self):
        self.clear_widgets()

        main_layout = MDBoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=20)

        title = MDLabel(
            text="ТЕМАТИЧЕСКИЕ МАРШРУТЫ",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.17, 0.09, 0.06, 1),
            font_style="H5",
            bold=True,
            size_hint=(1, 0.1)
        )

        scroll = MDScrollView()
        routes_box = MDBoxLayout(orientation='vertical', size_hint_y=None, spacing=15)
        routes_box.bind(minimum_height=routes_box.setter('height'))

        routes = [
            {"name": "ГОТИЧЕСКИЙ ВЫБОРГ", "color": "#615646", "points": "1, 3, 5, 6"},
            {"name": "ЛИТЕРАТУРНЫЙ МАРШРУТ", "color": "#443540", "points": "2, 4, 7"},
            {"name": "АРХИВНЫЕ НАХОДКИ", "color": "#2A3742", "points": "1, 2, 4, 7"}
        ]

        for route in routes:
            route_card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height=dp(120),
                padding=20,
                spacing=10,
                elevation=4,
                radius=[15],
                md_bg_color=(0.95, 0.93, 0.88, 1)
            )

            route_title = MDLabel(
                text=route['name'],
                theme_text_color="Custom",
                text_color=route["color"],
                bold=True
            )

            route_desc = MDLabel(
                text=f"Локации: {route['points']}",
                theme_text_color="Custom",
                text_color=(0.5, 0.4, 0.3, 1)
            )

            route_card.add_widget(route_title)
            route_card.add_widget(route_desc)
            routes_box.add_widget(route_card)

        scroll.add_widget(routes_box)

        back_btn = MDRaisedButton(
            text="<<- НАЗАД",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#8988CF",
            size_hint=(0.3, 0.08),
            on_release=lambda instance: self.go_to_map()
        )

        main_layout.add_widget(title)
        main_layout.add_widget(scroll)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def go_to_map(self):
        self.manager.current = "map"

class DiaryScreen(MDScreen):
    def on_enter(self):
        self.build_interface()

    def build_interface(self):
        self.clear_widgets()

        main_layout = MDBoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=20)

        title = MDLabel(
            text="МОЙ ДНЕВНИК",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.17, 0.09, 0.06, 1),
            font_style="H5",
            bold=True,
            size_hint=(1, 0.1)
        )

        content = MDLabel(
            text="Здесь будут сохраняться\nпосещенные места и любимые цитаты.",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.5, 0.4, 0.3, 1),
            font_style="H6"
        )

        back_btn = MDRaisedButton(
            text="← НАЗАД",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#8988CF",
            size_hint=(0.3, 0.08),
            on_release=lambda instance: self.go_to_map()
        )

        main_layout.add_widget(title)
        main_layout.add_widget(content)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def go_to_map(self):
        self.manager.current = "map"

class AboutScreen(MDScreen):
    def on_enter(self):
        self.build_interface()

    def build_interface(self):
        self.clear_widgets()

        main_layout = MDBoxLayout(orientation='vertical', padding=[30, 50, 30, 30], spacing=20)

        title = MDLabel(
            text="О ПРОЕКТЕ",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.17, 0.09, 0.06, 1),
            font_style="H5",
            bold=True,
            size_hint=(1, 0.1)
        )

        description = MDLabel(
            text="""«Город в литературных цитатах» — интерактивный путеводитель по Выборгу.

Проект представляет 7 ключевых локаций города, каждая из которых сопровождается:
• Исторической справкой
• Подлинными литературными цитатами
• Художественными образами

Цель проекта — показать Выборг глазами писателей и поэтов разных эпох.""",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.4, 0.3, 0.2, 1),
            size_hint_x=1,
            text_size=(None, None)
        )
        description.bind(texture_size=description.setter('size'))

        back_btn = MDRaisedButton(
            text="<<- НАЗАД",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color="#8988CF",
            size_hint=(0.3, 0.08),
            on_release=lambda instance: self.go_to_map()
        )

        main_layout.add_widget(title)
        main_layout.add_widget(description)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def go_to_map(self):
        self.manager.current = "map"

class LiteraryVyborgApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_landmark = LANDMARKS[0]

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"

        sm = MDScreenManager()
        sm.add_widget(MapScreen(name="map"))
        sm.add_widget(LandmarkScreen(name="landmark"))
        sm.add_widget(RoutesScreen(name="routes"))
        sm.add_widget(DiaryScreen(name="diary"))
        sm.add_widget(AboutScreen(name="about"))

        return sm

if __name__ == "__main__":
    LiteraryVyborgApp().run()