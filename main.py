from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class customweather(MDApp):
    def build(self):
        return MDLabel(text="Weather", halign="center")


customweather().run()