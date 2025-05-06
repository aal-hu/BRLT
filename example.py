from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.utils import platform
from kivy.app import App
import os
import shutil

KV = """
<MainScreen>:
    name: "main"
    MDFloatLayout:
        Image:
            id: bg_image
            source: root.bg_source
            allow_stretch: True
            keep_ratio: False
            size: self.parent.size
            pos: self.parent.pos

        MDRaisedButton:
            text: "Háttérkép cseréje"
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            on_release: root.open_file_manager()
"""


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Beállított háttérkép elérési útja
        self.bg_path = self.get_background_path()
        self.bg_source = self.bg_path if os.path.exists(self.bg_path) else "default_bg.jpg"

        # Fájlkezelő inicializálása
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".png", ".jpg", ".jpeg"]
        )

    def get_background_path(self):
        # Mentési hely platformfüggően
        if platform == "android":
            return os.path.join(App.get_running_app().user_data_dir, "hatter.jpg")
        else:
            return os.path.join("data", "hatter.jpg")

    def open_file_manager(self):
        start_path = os.path.expanduser("~") if platform != "android" else "/sdcard/"
        self.file_manager.show(start_path)

    def select_path(self, path: str):
        # háttérkép frissítése
        self.ids.bg_image.source = path

        # fájl mentése állandó helyre
        try:
            shutil.copy(path, self.bg_path)
            print(f"Sikeresen mentve: {self.bg_path}")
        except Exception as e:
            print(f"Hiba mentés közben: {e}")

        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MyApp().run()

