import kivy

kivy.require("2.1.0")
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
import os


KV = """
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        on_ref_press: app.on_ref_press(*args)
"""

class FakeModalView:
    def open(self):
        pass

    def dismiss(self):
        pass

class TreeTab(MDFloatLayout, MDTabsBase):
    """Class implementing file system browser."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        self.file_manager._window_manager = FakeModalView()  # replace the ModalView that the file manager uses

    def file_manager_open(self):
        self.add_widget(self.file_manager)  # just add the file manager to the tab
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        """
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class Ron(MDApp):
    @staticmethod
    def close_title(title):
        return f"[ref={title}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {title}"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
        tree_tab = TreeTab(title="Files")
        self.root.ids.tabs.add_widget(tree_tab)
        tree_tab.file_manager_open()
        self.root.ids.tabs.add_widget(Tab(title=self.close_title("Book")))
        self.root.ids.tabs.add_widget(Tab(title=self.close_title("Details")))

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
