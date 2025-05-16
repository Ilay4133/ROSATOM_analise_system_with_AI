import flet as ft

filter_pressure_text_field=ft.TextField(value='',label="Разница давлений (Па)",label_style=ft.TextStyle(color='#ffffff'),
                                            width=345,cursor_color='#ffffff',border_radius=10,
                                            text_style=ft.TextStyle(color='#ffffff',size=18),
                                            border_width=2,selection_color='#0f74ab',cursor_width=4,
                                            bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                            border_color=ft.colors.with_opacity(0.5, '#3A4EB1'))

flow_user_analise_text=ft.Text(value="Поток:",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_600)
flow_user_analise_text_cont=ft.Container(content=flow_user_analise_text,
                                         bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                         height=60,width=345,border_radius=10,
                                         padding=ft.Padding(top=15,left=15,bottom=15,right=15))

filter_stat_user_analise_text=ft.Text(value="Состояние фильтра: ",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_600)
filter_stat_user_analise_text_cont=ft.Container(content=filter_stat_user_analise_text,
                                                bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                                height=80,width=345,border_radius=10,
                                         padding=ft.Padding(top=15,left=15,bottom=15,right=15))
user_manual_analise_start_but_text = ft.Text(value="Начать анализ",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_600)

