
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value="Hello world!")
    
    greeting_history = []
    history_text = ft.Text("История приветствий")

    history_visidle = True

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
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий"
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
 
    def toggle_history (_):
        nonlocal history_visidle
        history_visidle = not history_visidle
        history_text.visible = history_visidle
        if history_visidle:
            toggle_history_btn.text = "Скрыть историю"
        else:
            toggle_history_btn.text = "Показать историю"
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton(text='SEND', on_click=on_button_click)
    clear_history_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme, tooltip='Сменить тему')

    toggle_history_btn = ft.ElevatedButton(text="Скрыть историю", on_click=toggle_history)

    page.add(greeting_text,name_input,name_button,clear_history_btn,theme_button,toggle_history_btn,history_text)

ft.app(target=main)  
