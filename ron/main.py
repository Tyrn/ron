"""
Audio Book Player for Linux and Android.
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

class Ron(MDApp):
    pass

if __name__ == "__main__":
    Ron().run()
