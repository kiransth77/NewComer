import kivy
from kivy.app import App
from kivy.uix.label import Label
from newcomer import ml_model as ml
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


    
class ChatUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.chat_history = TextInput(multiline=True, readonly=True)
        self.add_widget(self.chat_history)

        self.message_input = TextInput(multiline=False)
        self.add_widget(self.message_input)

        self.send_button = Button(text='Send', on_press=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, instance):
        self.send_button.disabled = True
        message = self.message_input.text
        # $PLACEHOLDER$ - Add code to send the message to the chat API
        self.message_input.text = ''
        response = ml.get_suggestion(message)
        self.chat_history.text += f'You: {message}\nBot: {response}\n'
        self.send_button.disabled = False

class MyApp(App):
    def build(self):
        self.title = 'NewComer App'
        return ChatUI()

if __name__ == '__main__':
    MyApp().run()
