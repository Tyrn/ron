"""
Power supply manager for Linux and Android.
"""
import kivy

kivy.require("2.1.0")
from kivy.utils import platform

from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

import weakref
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
import co_lang
from co_lang import T
import gc
import os

USERPATH = os.path.expanduser("~")

if platform == "android":
    from android.storage import primary_external_storage_path
    from android.storage import secondary_external_storage_path
    from android.permissions import request_permissions, Permission

    USERPATH = primary_external_storage_path()
    # USERPATH = secondary_external_storage_path()
    request_permissions(
        [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
    )


ACTION_ICON = "eye"


class TabList(FloatLayout, MDTabsBase):
    """The engaged power supplies tab."""

    def selected(self, filename):
        print(f"SeleCteD: {filename}")

    def surfacing(self, tab_text):
        pass


class TabDetails(FloatLayout, MDTabsBase):
    """The engaged power supply details tab."""

    def surfacing(self, tab_text):
        pass


class Ron(MDApp):
    menu_main = ObjectProperty()

    def menu_main_open(self, button):
        self.menu_main.caller = button
        self.menu_main.open()

    about_dialog = ObjectProperty()

    def about_dialog_close(self, *args):
        self.about_dialog.dismiss(force=True)

    def menu_item_about_callback(self, text):
        self.menu_main.dismiss()
        self.about_dialog = MDDialog(
            title=T("co-app-name"),
            size_hint=(0.8, 0.3),
            text=T("co-app-running-on") + f" {platform}",
            buttons=[
                MDFlatButton(
                    text=T("co-close-button"),
                    on_release=self.about_dialog_close,
                ),
            ],
        )
        self.about_dialog.open()

    def menu_main_build(self):
        items = [
            {
                "viewclass": "OneLineListItem",
                "text": T("co-about"),
                "height": dp(48),
                "on_release": lambda x=T("co-about"): self.menu_item_about_callback(x),
            }
        ]
        self.menu_main = MDDropdownMenu(
            width_mult=3,
            items=items,
            caller=self.root.ids.ps_toolbar.ids.right_actions.children[2],
        )

    menu_lang = ObjectProperty()

    def menu_locale_open(self, button):
        self.menu_lang.caller = button
        self.menu_lang.open()

    def menu_item_lang_callback(self, lng):
        self.menu_lang.dismiss()
        co_lang.set_language(lng)
        store = JsonStore("co_T.json")
        store.put("co-lang", name=lng)

    def menu_locale_build(self):
        items = []
        for lng in co_lang.languages():
            items.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": lng,
                    "height": dp(48),
                    "on_release": lambda x=lng: self.menu_item_lang_callback(x),
                }
            )
        self.menu_lang = MDDropdownMenu(
            width_mult=2,
            items=items,
            caller=self.root.ids.ps_toolbar.ids.right_actions.children[1],
        )

    @staticmethod
    def select_tab(destination_tab):
        tabs = MDApp.get_running_app().root.ids.ps_tabs
        # Just like your on_release.
        tabs.tab_bar.parent.dispatch(
            "on_tab_switch",
            destination_tab,
            destination_tab.tab_label,
            "Tab Text",
        )
        tabs.tab_bar.parent.carousel.load_slide(destination_tab)

    def build(self):
        co_lang.set_language("EN")
        store = JsonStore("co_T.json")
        if store.exists("co-lang"):
            lng = store.get("co-lang")["name"]
            co_lang.set_language(lng)

        return Builder.load_file("main.kv")

    def on_start(self):
        self.theme_cls.primary_palette = "Gray"
        # self.theme_cls.primary_hue = '900'
        self.theme_cls.material_style = "M3"
        if platform != "android":
            self.root.ids.ps_tabs.lock_swiping = True

        self.root.ids.ps_filechooser.rootpath = USERPATH

        def on_start(interval):
            self.menu_main_build()
            self.menu_locale_build()

        Clock.schedule_once(on_start)
        # Clock.schedule_once(lambda dt: self.discovery_request(30, 5), 5)

    def dir_deploy_book(self):
        pass

    def file_deploy_book(self):
        pass

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        """Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        """

        instance_tab.surfacing(tab_text)


if __name__ == "__main__":
    Ron().run()
