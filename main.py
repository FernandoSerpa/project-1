from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class AudioApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Crie cinco botões, cada um com uma função de tocar um áudio diferente
        audio_files = ['audio1.mp3', 'audio2.mp3', 'audio3.mp3', 'audio4.mp3', 'audio5.mp3']
        buttons = []
        for i, audio_file in enumerate(audio_files):
            button = Button(text=f'Áudio {i + 1}')
            button.bind(on_press=lambda instance, audio_file=audio_file: self.play_audio(audio_file))
            buttons.append(button)

        # Adicione os botões ao layout
        for button in buttons:
            layout.add_widget(button)

        return layout

    def play_audio(self, audio_file):
        sound = SoundLoader.load(audio_file)
        if sound:
            sound.play()


if __name__ == '__main__':
    AudioApp().run()