import flet as ft




filter_info_cont=ft.Container(content=None,width=341,height=436)


pressure_inf_text=ft.Text(value="Давление",color='#ffffff',font_family='Manrope',size=20,
                       weight=ft.FontWeight.W_500)
flow_inf_text=ft.Text(value="Поток",color='#ffffff',font_family='Manrope',size=20,
                       weight=ft.FontWeight.W_500)
filter_qu_inf=ft.Text(value="Состояние\n"
                            "фильтра ",color='#ffffff',font_family='Manrope',size=20,
                       weight=ft.FontWeight.W_500)
filter_temp_usin_inf=ft.Text(value="Температура\n"
                                   "эксплуатации ",color='#ffffff',font_family='Manrope',size=19,
                       weight=ft.FontWeight.W_500)
filter_performance_inf=ft.Text(value="Производи\nтельность ",color='#ffffff',font_family='Manrope',size=20,
                       weight=ft.FontWeight.W_500)


pressure_inf_text_cont_info=ft.Text(value="5 кПа",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
pressure_inf_text_cont=ft.Container(content=pressure_inf_text_cont_info,width=76,height=26,
                                    border_radius=5, bgcolor='#00A5FF',alignment=ft.Alignment(0,-1))
pressure_inf_row=ft.Row(controls=[pressure_inf_text,pressure_inf_text_cont],spacing=130)
pressure_inf_cont=ft.Container(content=pressure_inf_row,height=146,width=341,

                                  padding=ft.Padding(left=14,bottom=14,right=14,top=14),border_radius=10,
                               alignment=ft.Alignment(-1,-1))

graf_pressure_img=ft.Image(src="C:/Users/artem/PycharmProjects/PythonProject/ef4cb256-a19f-47c7-af0c-9ae0f23b0e8b-Photoroom.png",
                           width=311,height=88,fit=ft.ImageFit.CONTAIN)

graf_pressure_img_cont=ft.Container(content=graf_pressure_img,height=146,width=341,
                                    alignment=ft.Alignment(0,1))

pressure_inf_stack=ft.Stack(controls=[pressure_inf_cont,graf_pressure_img_cont],alignment=ft.Alignment(0,1))


flow_inf_text_cont_info=ft.Text(value="no data",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
flow_inf_text_cont=ft.Container(content=flow_inf_text_cont_info,width=89,height=26,
                                    border_radius=5, bgcolor='#00A5FF',alignment=ft.Alignment(0,-1))
flow_inf_column=ft.Column(controls=[flow_inf_text,flow_inf_text_cont],spacing=3)
flow_inf_column_cont=ft.Container(content=flow_inf_column,height=151,width=164,
                                  bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                  padding=ft.Padding(left=14,bottom=14,right=14,top=14),border_radius=10)

filter_qu_inf_cont_info=ft.Text(value="no%",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
filter_qu_inf_cont=ft.Container(content=filter_qu_inf_cont_info,width=60,height=24,
                                    border_radius=5, bgcolor='#00A5FF',alignment=ft.Alignment(0,-1))
filter_qu_inf_column=ft.Column(controls=[filter_qu_inf,filter_qu_inf_cont],spacing=3)
filter_qu_inf_column_cont=ft.Container(content=filter_qu_inf_column,height=151,width=164,
                                       bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                  padding=ft.Padding(left=14,bottom=14,right=14,top=14),border_radius=10)

filter_temp_usin_cont_info=ft.Text(value="100 °С",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
filter_temp_usin_cont=ft.Container(content=filter_temp_usin_cont_info,width=68.75,height=24,
                                    border_radius=5, bgcolor='#00A5FF',alignment=ft.Alignment(0,-1))
filter_temp_usin_column=ft.Column(controls=[filter_temp_usin_inf,filter_temp_usin_cont],spacing=3)
filter_temp_usin_column_cont=ft.Container(content=filter_temp_usin_column,height=151,width=164,
                                          bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                  padding=ft.Padding(left=14,bottom=14,right=14,top=14),border_radius=10)

filter_performance_cont_info=ft.Text(value="800 м³/ч",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
filter_performance_cont=ft.Container(content=filter_performance_cont_info,width=105,height=24,
                                    border_radius=5, bgcolor='#00A5FF',alignment=ft.Alignment(0,-1))
filter_performance_column=ft.Column(controls=[filter_performance_inf,filter_performance_cont],spacing=3)
filter_performance_column_cont=ft.Container(content=filter_performance_column,height=151,width=164,
                                            bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                  padding=ft.Padding(left=14,bottom=14,right=14,top=14),border_radius=10)

filter_name=ft.Text(value="Фильтр №1",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_700)
filter_name_cont=ft.Container(content=filter_name,width=800)

flow_value_variability=ft.Text(value="235-242",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_400)
flow_value_variability_cont=ft.Container(content=flow_value_variability,height=151,width=164,
                                         padding=ft.Padding(top=0,bottom=10,right=15,left=0),
                                         alignment=ft.Alignment(1,1))
flow_stack=ft.Stack(controls=[flow_inf_column_cont,flow_value_variability_cont],
                    alignment=ft.Alignment(1,1))

filter_qu_value_variability=ft.Text(value="0-100",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_400)
filter_qu_value_variability_cont=ft.Container(content=filter_qu_value_variability,height=151,width=164,
                                         padding=ft.Padding(top=0,bottom=10,right=15,left=0),
                                         alignment=ft.Alignment(1,1))
filter_qu_stack=ft.Stack(controls=[filter_qu_inf_column_cont,filter_qu_value_variability_cont],
                    alignment=ft.Alignment(1,1))

filter_temp_usin_value_variability=ft.Text(value="80-100",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_400)
filter_temp_usin_value_variability_cont=ft.Container(content=filter_temp_usin_value_variability,height=151,width=164,
                                         padding=ft.Padding(top=0,bottom=10,right=15,left=0),
                                         alignment=ft.Alignment(1,1))
filter_temp_usin_stack=ft.Stack(controls=[filter_temp_usin_column_cont,filter_temp_usin_value_variability_cont],
                    alignment=ft.Alignment(1,1))

filter_performance_value_variability=ft.Text(value="10-1000",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_400)
filter_performance_value_variability_cont=ft.Container(content=filter_performance_value_variability,height=151,width=164,
                                         padding=ft.Padding(top=0,bottom=10,right=15,left=0),
                                         alignment=ft.Alignment(1,1))
filter_performance_stack=ft.Stack(controls=[filter_performance_column_cont,filter_performance_value_variability_cont],
                    alignment=ft.Alignment(1,1))



srok_using_text=ft.Text(value="Срок использования",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_500)
srok_using_val=ft.Text(value="установлен 01.01.2022 (3 года)",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_200)
srok_using_column=ft.Column(controls=[srok_using_text,srok_using_val],
                            spacing=1)

filter_place_text=ft.Text(value="Место расположения",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_500)
filter_place_val=ft.Text(value="Сектор B",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_200)
filter_place_column=ft.Column(controls=[filter_place_text,filter_place_val],
                              spacing=1)

filtering_method_text=ft.Text(value="Метод очистки",color='#ffffff',font_family='Manrope',size=20,
                          weight=ft.FontWeight.W_500)
filtering_method_val=ft.Text(value="дистилляция",color='#ffffff',font_family='Manrope',size=15,
                          weight=ft.FontWeight.W_200)
filtering_method_column=ft.Column(controls=[filtering_method_text,filtering_method_val],
                                  spacing=1)

all_filtres_cong_column=ft.Column(controls=[srok_using_column,filter_place_column,filtering_method_column])






