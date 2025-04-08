import flet as ft
from frontend.filter_page_elements import *
from backend.database import *
from frontend.filters_seting_elements import *
import time as tm
from backend.telegram_bot import *
from frontend.user_analise_elements import *


def main(page: ft.Page):
    page.title="Моя АЭС"
    page.theme_mode=ft.ThemeMode.DARK
    page.bgcolor='#03050F'
    page.window.height=852
    page.window.width=393
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding=ft.Padding(left=0,bottom=0,right=0,top=0)
    page.fonts = {
        "Manrope": "C:/Users/artem/PycharmProjects/PythonProject/Manrope-VariableFont_wght.ttf",
    }
    page.window.resizable = False
    page.update()

    def open_filter1_config(e):
        filter_info_cont.visible = True
        filters_column.visible = False
        user_filter_analise_but.visible = False
        page.update()

    def back_to_filters(e):
        filter_info_cont.visible = False
        filters_column.visible = True
        user_filter_analise_but.visible = True
        page.update()


    def open_user_filter_analise(e):
        filters_column.visible = False
        user_filter_analise_but.visible = False
        filter_analise_column.visible = True
        page.update()

    def close_user_filter_analise(e):
        filters_column.visible = True
        user_filter_analise_but.visible = True
        filter_analise_column.visible = False
        page.update()


    def get_values_from_backend():
        while True:
            filter_values=save_to_database()
            pressure_inf_text_cont_info.value = str(int(filter_values[3]) // 1000)+" кПа"
            filter1_qu_text.value = str(int(filter_values[3]) // 1000) + " кПа"
            if filter_pressure_text_field.value !='':
                filter_pressure_val = int(filter_pressure_text_field.value)
                if filter_pressure_val <= 5000:
                    filter_status = "100%"
                    flow_user_analise_text.value="Поток: 242 кг/с"
                    filter_stat_user_analise_text.value="Состояние фильтра: " + filter_status
                    flow_user_analise_text_cont.bgcolor = '#00A5FF'
                    filter_stat_user_analise_text_cont.bgcolor = '#00A5FF'

                elif filter_pressure_val > 500 and filter_pressure_val < 10000:
                    con = (1 - (filter_pressure_val - 5000) / 5000) * 100
                    filter_status = str(con) + "%"
                    flow_user_analise_text.value = "Поток: 241 кг/с"
                    filter_stat_user_analise_text.value = "Состояние фильтра: " + filter_status
                    flow_user_analise_text_cont.bgcolor = '#C5671F'
                    filter_stat_user_analise_text_cont.bgcolor = '#C5671F'

                elif filter_pressure_val >= 10000:
                    filter_status = "0%"
                    flow_user_analise_text.value = "Поток: 239 кг/с"
                    filter_stat_user_analise_text.value = "Состояние фильтра: " + filter_status
                    flow_user_analise_text_cont.bgcolor='#AF0D0D'
                    filter_stat_user_analise_text_cont.bgcolor='#AF0D0D'

            if filter_values[3]<5000:
                pressure_inf_text_cont_info.value = "5" + " кПа"
                filter1_qu_text.value = "5" + " кПа"
            else:
                pressure_inf_text_cont_info.value = str(int(filter_values[3]) // 1000) + " кПа"
                filter1_qu_text.value = str(int(filter_values[3]) // 1000) + " кПа"

            if int(filter_values[3])>5000 and int(filter_values[3])<10000:
                send_metrics(
                    pressure=float(filter_values[3]),
                    flow=float(filter_values[2]),
                    filter_status=float(filter_values[1])
                )
                filter_qu1_cont.bgcolor='#C5671F'
                filter_qu_inf_cont.bgcolor='#C5671F'
                pressure_inf_text_cont.bgcolor='#C5671F'
                page.update()

            elif int(filter_values[3])>=10000:
                send_metrics(
                    pressure=float(filter_values[3]),
                    flow=float(filter_values[2]),
                    filter_status=float(filter_values[1])
                )
                filter_qu1_cont.bgcolor='#AF0D0D'
                filter_qu_inf_cont.bgcolor='#AF0D0D'
                pressure_inf_text_cont.bgcolor='#AF0D0D'
                page.update()

            flow_inf_text_cont_info.value = str(int(filter_values[2])//1)+" кг/с"
            filter_qu_inf_cont_info.value = str(filter_values[1]//1)+"%"
            page.update()
            tm.sleep(10)
            '''
            tm.sleep(x) - настройка, как часто
            будет проходить анализ фильтра 
            в x секундах
            '''

    filter1_list_tile = ft.ElevatedButton(content=filter1_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341,on_click=open_filter1_config)
    filters_column=ft.Column(controls=[all_filters_text_cont,filter1_list_tile,filter2_list_tile,filter3_list_tile,filter4_list_tile
                                       ,filter5_list_tile],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                             alignment=ft.MainAxisAlignment.CENTER)

    return_to_filtres_icon_but=ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN_ROUNDED,icon_size=30,icon_color='#00A5FF',
                                             on_click=back_to_filters)
    return_to_filtres_icon_but_cont=ft.Container(content=return_to_filtres_icon_but,width=341,bgcolor=None,
                                                 alignment=ft.Alignment(-1,0))


    all_filters_info_column = ft.Column(controls=[filter_name_cont,pressure_inf_but,
                            ft.Row(controls=[flow_stack, filter_qu_stack]),
                            ft.Row(controls=[filter_temp_usin_stack,filter_performance_stack]),
                            return_to_filtres_icon_but_cont],
                                        horizontal_alignment=ft.CrossAxisAlignment.START,spacing=20)
    filter_info_cont = ft.Container(content=all_filters_info_column)

    user_filter_analise_but_text=ft.Text(value="Анализ фильтра",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_700)

    return_to_filtres_icon_but_from_analise = ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN_ROUNDED, icon_size=30,
                                               icon_color='#00A5FF',
                                               on_click=close_user_filter_analise)
    return_to_filtres_icon_but_cont_from_analise = ft.Container(content=return_to_filtres_icon_but_from_analise, width=341, bgcolor=None,
                                                   alignment=ft.Alignment(-1, 0))

    user_filter_analise_but = ft.ElevatedButton(content=user_filter_analise_but_text,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341,on_click=open_user_filter_analise)

    filter_analise_column=ft.Column(controls=[filter_pressure_text_field,
                                              flow_user_analise_text_cont,filter_stat_user_analise_text_cont,
                                              return_to_filtres_icon_but_cont_from_analise])
    filter_analise_cont=ft.Container(content=filter_analise_column,)

    all_page_filters_column=ft.Column(controls=[logo_container,filters_column,
                                                filter_info_cont,user_filter_analise_but,filter_analise_cont],
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                             alignment=ft.MainAxisAlignment.CENTER)

    all_page_cont=ft.Container(content=all_page_filters_column,padding=ft.Padding(left=20,right=20,top=30,bottom=20),
                               alignment=ft.alignment.center)

    page_bg_img=ft.Image(src="C:/Users/artem/PycharmProjects/PythonProject/app_background.jpg",
                         height=846, width=393, fit=ft.ImageFit.CONTAIN)

    all_page_stack=ft.Stack(controls=[page_bg_img,all_page_cont])
    page.add(all_page_stack)
    page.update()
    close_user_filter_analise(1)
    back_to_filters(1)
    get_values_from_backend()

ft.app(target=main)

