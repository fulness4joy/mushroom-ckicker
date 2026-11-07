from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MushroomClickerApp(App):
    def build(self):
        self.title = "MushroomClicker!"

        btn_play = Button(text="Play", font_size=30)
        btn_settings = Button(text="Settings", font_size=30)
        title_label = Label(text="MushroomClicker", font_size=40)

        box = BoxLayout(orientation = 'vertical', padding=20, spacing=10)
        box.add_widget(title_label)
        box.add_widget(btn_settings)
        box.add_widget(btn_play)

        return box


app = MushroomClickerApp()
app.run()