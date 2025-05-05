import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])


class MainScreen(MDScreen):
    bg_source = "image.png"
    labeltxt = StringProperty()    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        self.load_counter()
        self.update_label()
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".png", ".jpg", ".jpeg"],
            preview=True
        )

    def open_file_manager(self):
        start_path = os.path.expanduser("~")  # kezdőkönyvtár
        self.file_manager.show(start_path)

    def select_path(self, path: str):
        self.ids.bg_image.source = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()
   
    def load_counter(self):
        try:
            with open('counter.txt', 'r') as file:
                self.counter = int(file.read())
        except (FileNotFoundError, ValueError):
            self.counter = 0
            self.save_counter()
        #self.update_label()

    def update_label(self):
        self.labeltxt = 'Counter: '+str(self.counter)

    def increment(self):
        if self.counter < 20:
            self.counter += 1
        self.update_label()
        self.save_counter()

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1
        self.update_label()
        self.save_counter()

    def save_counter(self):
        with open('counter.txt', 'w') as file:
            file.write(str(self.counter))
  

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return MainScreen()
   
  
if __name__ == '__main__':
    MyApp().run()