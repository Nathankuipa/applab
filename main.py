from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
MDScreen:
	MDLabel:
		halign: 'center'
		text: 'Hello World!'

"""
class MyApp(MDApp):
	def build(self):
		return Builder.load_string(kv)
	
if __name__ == "__main__":
	MyApp().run()