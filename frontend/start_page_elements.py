import flet as ft

start_page_logo=ft.Image(src='C:/Users/artem/PycharmProjects/PythonProject/start_logo.png',
                         width=223,height=235,fit=ft.ImageFit.CONTAIN)

input_code_text_field = ft.TextField(
    label="Ввести код",
    width=230,
    bgcolor=ft.colors.TRANSPARENT,
    border_width=0,
    focused_border_width=0,
    border_color=ft.colors.TRANSPARENT,
    focused_border_color=ft.colors.TRANSPARENT,
    hover_color=ft.colors.TRANSPARENT,
    content_padding=0,
    text_style=ft.TextStyle(
        color='#ffffff',
        bgcolor=ft.colors.TRANSPARENT,
        font_family='Manrope',size=20,
        weight=ft.FontWeight.W_600
    ),
    label_style=ft.TextStyle(
        color=ft.colors.with_opacity(0.5, '#ffffff'),
        bgcolor=ft.colors.TRANSPARENT,
        font_family='Manrope',size=20,
        weight=ft.FontWeight.W_500
    ),
    cursor_color='#ffffff',
    selection_color="#404040"
)
