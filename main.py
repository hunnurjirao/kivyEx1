import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout   
from kivy.uix.textinput import TextInput   
from kivy.uix.button import Button

 


class Hellopage(GridLayout): 

		def __init__(self, **kwargs):
			super().__init__(**kwargs)
			
			self.cols = 2

			self.add_widget(Label(text="Username"))
			self.username = TextInput(multiline=False)
			self.add_widget(self.username)

			self.add_widget(Label(text="Password"))
			self.password = TextInput(password=True,multiline=False)
			self.add_widget(self.password)
			
			self.press = Button(text="Click me")
			self.press.bind(on_press=self.click_me)
			self.add_widget(Label())
			self.add_widget(self.press)


		def click_me(self,instance):

			print(f"Username = {self.username.text}\nPassword = {self.password.text}")




				

class EpicApp(App):
    def build(self):
        return Hellopage()


if __name__ == "__main__":
    EpicApp().run()
