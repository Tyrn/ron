import kivy

kivy.require("2.1.0")
from kivy.utils import platform

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
import os

USERPATH = os.path.expanduser("~")

if platform == "android":
    from android.storage import primary_external_storage_path
    from android.storage import secondary_external_storage_path
    from android.permissions import request_permissions, Permission

    USERPATH = primary_external_storage_path()
    request_permissions(
        [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
    )


KV = """
#:kivy 2.1.0
#:set dark_gray (.5, .5, .5, 1)

MDBoxLayout:
    orientation: "vertical"
    MDTabs:
        id: ps_tabs
        TabList:
            id: ps_tab_list
            icon: "folder"
            FileChooserListView:
                id: ps_filechooser
                canvas.before:
                    Color:
                        rgba: dark_gray
                    Rectangle:
                        size: self.size
                        pos: self.pos
            MDFloatingActionButton:
                id: fc_playdir
                icon: "folder"
                pos_hint: {"center_x": .4, "center_y": .5}
            MDFloatingActionButton:
                id: fc_playfile
                icon: "file"
                pos_hint: {"center_x": .6, "center_y": .5}
        TabDetails:
            id: ps_tab_details
            icon: "book"
            MDScrollView:
"""


class TabList(FloatLayout, MDTabsBase):
    """The engaged power supplies tab."""


class TabDetails(FloatLayout, MDTabsBase):
    """The engaged power supply details tab."""


class Ron(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.material_style = "M3"
        if platform != "android":
            self.root.ids.ps_tabs.lock_swiping = True

        self.root.ids.ps_filechooser.rootpath = USERPATH


if __name__ == "__main__":
    Ron().run()
