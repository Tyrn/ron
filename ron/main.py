"""
Audio Book Player for Linux and Android.
"""
import kivy

kivy.require("2.1.0")
# from kivy.utils import platform

# from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder

# from kivy.properties import ObjectProperty
## from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.floatlayout import MDFloatLayout

# from kivy.uix.gridlayout import GridLayout

# import weakref
# from kivy.clock import Clock
from kivymd.app import MDApp

# from kivy.metrics import dp
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

# from kivymd.uix.list import IRightBodyTouch
# from kivymd.uix.list import TwoLineAvatarIconListItem
# from kivymd.uix.selectioncontrol import MDCheckbox
# from kivymd.uix.button import MDFlatButton
# from kivymd.uix.button import MDIconButton
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class Ron(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("main.kv")

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(
                Tab(
                    title=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {name_tab}"
                )
            )

    def on_ref_press(
        self,
        instance_tabs,
        instance_tab_label,
        instance_tab,
        instance_tab_bar,
        instance_carousel,
    ):
        """
        The method will be called when the ``on_ref_press`` event
        occurs when you, for example, use markup text for tabs.

        :param instance_tabs: <kivymd.uix.tab.MDTabs object>
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
        :param instance_tab: <__main__.Tab object>
        :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
        :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
        """

        # Removes a tab by clicking on the close icon on the left.
        for instance_tab in instance_carousel.slides:
            if instance_tab.title == instance_tab_label.text:
                instance_tabs.remove_widget(instance_tab_label)
                break


if __name__ == "__main__":
    Ron().run()
