import kivy
kivy.require("2.2.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CustomBtn(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print(f"pressed at {pos}")


class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text=" btn 1"))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text="btn 2"))

    def btn_pressed(self, instance, pos):
        print(f'pos: printed from root widget: {pos}')


class MyApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
