from kivy.properties import BooleanProperty, ColorProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.utils import rgba

from kivymd.color_definitions import colors as _colors
from kivymd.color_definitions import text_colors
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase


class KitchenSinkThemingColors(Screen):
    def on_enter(self):
        for color in _colors.keys():
            tab_widget = KitchenSinkThemeTab(text=str(color))
            self.ids.tabs_manager.add_widget(tab_widget)

    def on_tab_switch(
        self,
        instance_tab_manager,
        instance_android_tabs,
        instance_tab_label,
        tab_label_text,
    ):
        if not instance_android_tabs.colors_loaded:
            for hue in _colors[tab_label_text]:
                color = _colors[tab_label_text][hue]
                if tab_label_text == "Light":
                    text_color = (0, 0, 0, 1)
                elif tab_label_text == "Dark":
                    text_color = (1, 1, 1, 1)
                else:
                    text_color = text_colors[tab_label_text][hue]
                color_widget = {
                    "rgba_color": rgba(color),
                    "hex_color": color,
                    "hue_color": hue,
                    "text_color": text_color,
                }
                instance_android_tabs.rv.data.append(color_widget)
            instance_android_tabs.colors_loaded = True


class KitchenSinkColorWidget(MDBoxLayout):
    rgba_color = ColorProperty()
    text_color = ColorProperty()
    hex_color = StringProperty()
    hue_color = StringProperty()


class KitchenSinkThemeTab(MDBoxLayout, MDTabsBase):
    colors_loaded = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
