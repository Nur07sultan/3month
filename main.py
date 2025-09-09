
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value="Hello world!")
    
    greeting_history = []
    history_text = ft.Text("История приветствий")

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Hello {name}!"
            name_input.value = ''

            # Получаем текущее время
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Формируем запись с временем перед именем
            entry = f"{time_now} — {name}"

            # Добавляем в историю
            greeting_history.append(entry)
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, ведите имя!"

        page.update()
        
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton(text='SEND', on_click=on_button_click)

    page.add(greeting_text, name_input, name_button, history_text)

ft.app(target=main)

