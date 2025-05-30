
import threading
from rosatom_project.frontend.filter_page_elements import *
from rosatom_project.backend.database import *
from rosatom_project.frontend.filters_seting_elements import *
import time as tm
from rosatom_project.backend.telegram_bot import *
from rosatom_project.frontend.user_analise_elements import *
from rosatom_project.frontend.start_page_elements import *
from rosatom_project.backend.matplotlib_graph import *
from rosatom_project.frontend.graph_visual_elements import *

def main(page: ft.Page):
    page.title="Моя АЭС"
    page.theme_mode=ft.ThemeMode.DARK
    page.bgcolor='#03050F'
    page.window.height=872
    page.window.width=393
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding=ft.Padding(left=0,bottom=0,right=0,top=0)
    page.fonts = {
        "Manrope": "C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/Manrope-VariableFont_wght.ttf",
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
        filter_analise_cont.visible = True
        filters_column.visible = False
        user_filter_analise_but.visible = False
        filter_analise_column.visible = True
        page.update()

    def close_user_filter_analise(e):
        filter_analise_cont.visible = False
        filters_column.visible = True
        user_filter_analise_but.visible = True
        filter_analise_column.visible = False
        page.update()

    def open_dop_filter_inf(e):
        flow_stack.visible = False
        filter_qu_stack.visible = False
        filter_temp_usin_stack.visible = False
        filter_performance_stack.visible = False
        pressure_inf_but_cont.height = 525
        pressure_inf_but_cont.bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1')
        get_worker_help_but.visible = False
        if pressure_inf_text_cont.bgcolor=='#AF0D0D':
            pressure_inf_but_cont.height=590
            get_worker_help_but.visible = True
        all_filtres_cong_column.visible = False
        page.update()

    def close_dop_filter_inf(e):
        flow_stack.visible = True
        filter_qu_stack.visible = True
        filter_temp_usin_stack.visible = True
        filter_performance_stack.visible = True
        pressure_inf_but_cont.height = 146
        pressure_inf_but_cont.bgcolor = None
        all_filtres_cong_column.visible = True
        page.update()

    def all_close():
        qu_icon_but_cont.visible = False
        logo_container.visible = False
        filters_column.visible = False
        filter_info_cont.visible = False
        user_filter_analise_but.visible = False
        filter_analise_cont.visible = False
        cont3_code_auth_place.visible = False
        page.update()

    def open_code_auth(e):
        start_logo_but_cont.visible = False
        logo_container.visible = True
        cont3_code_auth_place.visible = True
        page.update()

    def open_all():
        qu_icon_but_cont.visible = True
        filters_column.visible = True
        cont3_code_auth_place.visible = False
        user_filter_analise_but.visible = True
        start_threads()
        page.update()


    def code_auth(e):
        code_val=input_code_text_field.value
        db = sqlite3.connect("C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/Rosatom.data")
        cur = db.cursor()
        cur.execute("SELECT * FROM Rosatom_users")
        data = cur.fetchall()
        if any(code_val in tupl for tupl in data):
            for row in data:
                if code_val == row[0]:
                    open_all()
                    dlg_get_worker_help = ft.AlertDialog(
                        title=ft.Column(controls=[ft.Text(value=f"Добро пожаловать {row[1]} {row[2]}", color='#ffffff',
                                                          font_family='Manrope', size=25, weight=ft.FontWeight.W_700),
                                                  ft.Text(value="Хорошей работы!",
                                                          color='#ffffff',
                                                          font_family='Manrope', size=17, weight=ft.FontWeight.W_500)
                                                  ]), bgcolor='#013DFD')
                    page.open(dlg_get_worker_help)
                    page.update()
        else:
            dlg_get_worker_help = ft.AlertDialog(
                title=ft.Column(controls=[ft.Text(value="Неверный код", color='#ffffff',
                                          font_family='Manrope', size=25, weight=ft.FontWeight.W_700),
                                          ft.Text(value="Повторите попытку\nвхода",
                                          color='#ffffff',
                                          font_family='Manrope', size=17, weight=ft.FontWeight.W_500)
                                          ]), bgcolor='#013DFD'
            )
            page.open(dlg_get_worker_help)
            page.update()
        db.close()




    def get_worker_help(e):
        dlg_get_worker_help=ft.AlertDialog(
            title=ft.Column(controls=[ft.Text(value="Работник вызван",color='#ffffff',
                                    font_family='Manrope',size=25,weight=ft.FontWeight.W_700),
                                      ft.Text(value="Вам придет уведомление\nо завершении проверки", color='#ffffff',
                                              font_family='Manrope', size=17, weight=ft.FontWeight.W_500)
                                      ]),bgcolor='#013DFD'
        )
        send_mail_need_help()
        page.open(dlg_get_worker_help)
        page.update()

    def get_values_from_backend1():
        while True:
            filter_values=save_to_database1()
            pressure_inf_text_cont_info.value = str(int(filter_values[3]) // 1)+" Па"
            filter1_qu_text.value = str(int(filter_values[3]) // 1) + " Па"

            if filter_values[3]<5000:
                pressure_inf_text_cont_info.value = "5000" + " Па"
                filter1_qu_text.value = "5000" + " Па"
            else:
                pressure_inf_text_cont_info.value = str(int(filter_values[3]) //1) + " Па"
                filter1_qu_text.value = str(int(filter_values[3]) //1) + " Па"

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
            tm.sleep(60)


    def user_manual_filter_analise(e):
        if filter_pressure_text_field.value != '':
            filter_pressure_val = int(filter_pressure_text_field.value)
            if filter_pressure_val <= 5000:
                filter_status = "100%"
                flow_user_analise_text.value = f"Поток:{filter_pressure_val * 0.0485} кг/с"
                filter_stat_user_analise_text.value = "Состояние фильтра: " + filter_status
                flow_user_analise_text_cont.bgcolor = '#00A5FF'
                filter_stat_user_analise_text_cont.bgcolor = '#00A5FF'
            elif filter_pressure_val > 5000 and filter_pressure_val < 10000:
                con = (1 - (filter_pressure_val - 5000) / 5000) * 100
                filter_status = str(con) + "%"
                flow_user_analise_text.value = f"Поток:{242.5 - filter_pressure_val * 0.00003} кг/с"
                filter_stat_user_analise_text.value = "Состояние фильтра: " + filter_status
                flow_user_analise_text_cont.bgcolor = '#C5671F'
                filter_stat_user_analise_text_cont.bgcolor = '#C5671F'
            elif filter_pressure_val >= 10000:
                filter_status = "0%"
                flow_user_analise_text.value = f"Поток:{242.5 - filter_pressure_val * 0.00003} кг/с"
                filter_stat_user_analise_text.value = "Состояние фильтра: " + filter_status
                flow_user_analise_text_cont.bgcolor = '#AF0D0D'
                filter_stat_user_analise_text_cont.bgcolor = '#AF0D0D'
        page.update()

    def start_threads():
        math_and_ai_model_thread1 = threading.Thread(target=get_values_from_backend1)
        math_and_ai_model_thread1.start()

    #def graph_visual_open(e):
    #    open_matplotlib_graph()
    #    dlg_get_worker_help = ft.BottomSheet(graph_img, bgcolor='#013DFD')
    #    page.open(dlg_get_worker_help)
    #    page.update()


    graph_open_icon_but1 = ft.IconButton(icon=ft.Icons.AUTO_GRAPH_ROUNDED, icon_size=30, icon_color='#00bbff', on_click=lambda e: graph_visual_open(e, page))
    filter1_but_cont = ft.Row(controls=[filter1_name_text, ft.Row(controls=[graph_open_icon_but1,filter_qu1_cont])], spacing=87)

    filter1_list_tile = ft.ElevatedButton(content=filter1_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341,on_click=open_filter1_config)

    filter2_list_tile = ft.ElevatedButton(content=filter2_but_cont, bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46, width=341,on_click=open_filter1_config)

    filter3_list_tile = ft.ElevatedButton(content=filter3_but_cont, bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46, width=341,on_click=open_filter1_config)

    filter4_list_tile = ft.ElevatedButton(content=filter4_but_cont, bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46, width=341,on_click=open_filter1_config)

    filter5_list_tile = ft.ElevatedButton(content=filter5_but_cont, bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46, width=341,on_click=open_filter1_config)

    filters_column=ft.Column(controls=[all_filters_text_cont,filter1_list_tile,filter2_list_tile,filter3_list_tile,filter4_list_tile
                                       ,filter5_list_tile],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                             alignment=ft.MainAxisAlignment.CENTER)

    return_to_filtres_icon_but=ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN_ROUNDED,icon_size=30,icon_color='#00A5FF',
                                             on_click=back_to_filters)
    return_to_filtres_icon_but_cont=ft.Container(content=return_to_filtres_icon_but,width=30,bgcolor=None,
                                                 alignment=ft.Alignment(-1,0))

    pressure_inf_but = ft.ElevatedButton(content=pressure_inf_stack, height=146, width=341,
                                         bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                         style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                         on_click=open_dop_filter_inf,on_long_press=close_dop_filter_inf)

    problem_solving_recomend_text=ft.Text(value="Рекомендации",color='#ffffff',
                                    font_family='Manrope',size=20,weight=ft.FontWeight.W_500)

    problem_solving_text = ft.Text(value="• Провести регулярные проверки\n"
                                         "фильтров на наличие загрязнений и\n"
                                         "износа.\n"
                                         "• Оценить производительность насосов\n"
                                         "и их соответствие требованиям\n"
                                         "системы. \n"
                                         "• Убедиться в отсутствии утечек в\n"
                                         "системе, которые могут влиять на\n"
                                         "давление.",
                                   color=ft.colors.with_opacity(0.8, '#ffffff'),
                                      font_family='Manrope', size=15, weight=ft.FontWeight.W_300)

    diapozons = ft.Text(value="Диапазоны", color='#ffffff',font_family='Manrope',
                        size=20, weight=ft.FontWeight.W_500)
    diapozons_row=ft.Row(controls=[diapozons],width=306)

    normal_pressure_val_text = ft.Text(value="Норма", color='#ffffff',
                                      font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    normal_pressure_val = ft.Text(value="5000-10000", color='#ffffff',
                                       font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    normal_pressure_row=ft.Row(controls=[normal_pressure_val_text,normal_pressure_val],spacing=170,width=306)

    min_pressure_val_text = ft.Text(value="Минимальное", color='#ffffff',
                                      font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    min_pressure_val = ft.Text(value="5000", color='#ffffff',
                                    font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    min_pressure_row = ft.Row(controls=[min_pressure_val_text, min_pressure_val], spacing=165, width=306)

    max_pressure_val_text = ft.Text(value="Максимальное", color='#ffffff',
                                      font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    max_pressure_val = ft.Text(value="более 10000", color='#ffffff',
                                    font_family='Manrope', size=15, weight=ft.FontWeight.W_400)
    max_pressure_row = ft.Row(controls=[max_pressure_val_text, max_pressure_val], spacing=105, width=306)

    get_worker_help_but_text=ft.Text(value="Вызвать работника", color='#ffffff',
                                    font_family='Manrope', size=25, weight=ft.FontWeight.W_700)
    get_worker_help_but=ft.ElevatedButton(content=get_worker_help_but_text,height=46,width=301,
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          bgcolor='#013DFD',
                                          on_click=get_worker_help)


    pressure_inf_column=ft.Column(controls=[pressure_inf_but,diapozons_row,
                                            normal_pressure_row,
                                            ft.Divider(color=ft.colors.with_opacity(0.23, '#ffffff'),
                                                       height=3,thickness=1),
                                            min_pressure_row,
                                            ft.Divider(color=ft.colors.with_opacity(0.23, '#ffffff'),
                                                       height=3,thickness=1),
                                            max_pressure_row,
                                            ft.Row(controls=[problem_solving_recomend_text],width=306),
                                            problem_solving_text,
                                            ft.Divider(color=ft.colors.with_opacity(0.5, '#3A4EB1')),
                                  get_worker_help_but],spacing=5,
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    pressure_inf_but_cont=ft.Container(content=pressure_inf_column, height=146, width=341,border_radius=10)

    all_filters_info_column = ft.Column(controls=[
                ft.Row(controls=[return_to_filtres_icon_but_cont,filter_name_cont],
                       spacing=20,width=360),
                            pressure_inf_but_cont,
                            ft.Row(controls=[flow_stack, filter_qu_stack]),
                            ft.Row(controls=[filter_temp_usin_stack,filter_performance_stack]),
                            all_filtres_cong_column],
                                        horizontal_alignment=ft.CrossAxisAlignment.START,spacing=20)
    filter_info_cont = ft.Container(content=all_filters_info_column)

    user_filter_analise_but_text=ft.Text(value="Анализ фильтра",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_700)

    user_mamual_analise_start_but = ft.ElevatedButton(content=user_manual_analise_start_but_text,
                                                      bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                                      style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                                      height=40, width=200, on_click=user_manual_filter_analise)

    return_to_filtres_icon_but_from_analise = ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN_ROUNDED, icon_size=30,
                                               icon_color='#00A5FF',
                                               on_click=close_user_filter_analise)

    end_analise_row=ft.Row(controls=[return_to_filtres_icon_but_from_analise,user_mamual_analise_start_but])
    return_to_filtres_icon_but_cont_from_analise = ft.Container(content=end_analise_row, width=341, bgcolor=None,
                                                   alignment=ft.Alignment(-1, 0))

    user_filter_analise_but = ft.ElevatedButton(content=user_filter_analise_but_text,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341,on_click=open_user_filter_analise)

    filter_analise_column=ft.Column(controls=[filter_pressure_text_field,
                                              flow_user_analise_text_cont,filter_stat_user_analise_text_cont,
                                              return_to_filtres_icon_but_cont_from_analise])
    filter_analise_cont=ft.Container(content=filter_analise_column)

    start_logo_but = ft.ElevatedButton(content=start_page_logo,
                                       style=ft.ButtonStyle(
                                           bgcolor=ft.colors.TRANSPARENT,
                                           shadow_color=ft.colors.TRANSPARENT,
                                           surface_tint_color=ft.colors.TRANSPARENT,
                                           overlay_color=ft.colors.TRANSPARENT,
                                           elevation=0), on_click=open_code_auth)

    code_auth_icon_but = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS_ROUNDED,
                                       icon_color='#ffffff', icon_size=24,
                                       on_click=code_auth)

    code_auth_row=ft.Row(controls=[input_code_text_field,code_auth_icon_but])

    cont1_code_auth = ft.Container(
        content=code_auth_row,
        height = 52, width = 301,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(
            width=1,
            color=ft.colors.with_opacity(0.5, '#ffffff')
        ),
        border_radius=10,
        padding=10, alignment=ft.Alignment(0,0))

    cont2_code_auth=ft.Container(
        content=cont1_code_auth,
        height=79, width=341,
        bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
        border_radius=10,
        alignment=ft.Alignment(0,0)
    )
    cont3_code_auth_place=ft.Container(content=cont2_code_auth,height=800,width=393,
                                       alignment=ft.Alignment(0, -0.2)
                                       )

    start_logo_but_cont=ft.Container(content=start_logo_but,height=872,width=393,
                                     alignment=ft.Alignment(0,-0.25))

    all_page_filters_column=ft.Column(controls=[start_logo_but_cont,logo_container,cont3_code_auth_place,filters_column,
                                                filter_info_cont,user_filter_analise_but,filter_analise_cont],
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                             alignment=ft.MainAxisAlignment.CENTER)

    all_page_cont=ft.Container(content=all_page_filters_column,padding=ft.Padding(left=20,right=20,top=30,bottom=20),
                               alignment=ft.alignment.center)

    page_bg_img=ft.Image(src="C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/app_background.jpg",
                         height=846, width=393, fit=ft.ImageFit.CONTAIN)

    all_page_stack=ft.Stack(controls=[page_bg_img,all_page_cont])

    qu_icon_but=ft.IconButton(icon=ft.Icons.QUESTION_MARK_ROUNDED,bgcolor='#3A4EB1',
                              icon_size=30, icon_color='#030264')
    qu_icon_but_cont=ft.Container(content=qu_icon_but, height=74,width=74,
                                  padding=ft.Padding(top=0,bottom=20,left=10,right=10))

    all_all_page_stack=ft.Stack(controls=[all_page_stack,qu_icon_but_cont],alignment=ft.Alignment(1,1))

    page.add(all_all_page_stack)
    page.update()
    close_user_filter_analise(1)
    back_to_filters(1)
    all_close()

ft.app(target=main)

#42kem_ra_x009017
