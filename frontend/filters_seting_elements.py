import flet as ft

logo_img=ft.Image(src="https://s3-alpha-sig.figma.com/img/8047/7f82/f5957c4a1d4b61d4ef2a98f226a0515f?Expires=1745193600&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=FtpUsHOm4udgasI-dlBInKDNMQkX08hb3~UxHEsekUikIBLn2UFvYRnrHkMs1Op03gFVNNgN104bL-DvkVI4nzA6slxkZWsXaM011-lcN9JN0-6GMU67mwLGCqzuwVD4jdHs7MgG1MipPnoutWzcScicXN7CVJEMvsc7S6IBaRgAQIJZlHmcCQtteuVKwpiW-uEsf452GbiOJeH9nNWUv268QCzhgCzRqfH0t04G2uTJmU8IMu3uqk9V0oL79NElWdBWiOsNYw8UTEXECnw79BX8pqnMjpUGPgJ7Rjf3sQKh09vq2G6pcoEsrmXUPa7ANI39Z5fd9Q9GkW3EtmHPBQ__"
                  ,height=26, width=128, fit=ft.ImageFit.CONTAIN)
logo_container=ft.Container(content=logo_img,height=31,width=138,bgcolor='#0055F8',
                            alignment=ft.alignment.center,border_radius=30)

all_filters_text=ft.Text(value="Все фильтры",color='#ffffff',size=20,
                         font_family='Manrope',weight=ft.FontWeight.W_600)

all_filters_text_cont=ft.Container(content=all_filters_text,alignment=ft.Alignment(-1,0),width=342)

filter1_qu_text=ft.Text(value="no data",color='#ffffff',font_family='Manrope',size=15,
                       weight=ft.FontWeight.W_700)
filter2_qu_text=ft.Text(value="5000 Па",color='#ffffff',font_family='Manrope',size=15,
                       weight=ft.FontWeight.W_700)
filter3_qu_text=ft.Text(value="7500 Па",color='#ffffff',font_family='Manrope',size=15,
                       weight=ft.FontWeight.W_700)
filter4_qu_text=ft.Text(value="11600 Па",color='#ffffff',font_family='Manrope',size=15,
                       weight=ft.FontWeight.W_700)
filter5_qu_text=ft.Text(value="5000 Па",color='#ffffff',font_family='Manrope',size=15,
                       weight=ft.FontWeight.W_700)

filter1_name_text=ft.Text(value="Фильтр №1",color='#ffffff',font_family='Manrope',size=16,
                          weight=ft.FontWeight.W_300)
filter2_name_text=ft.Text(value="Фильтр №2",color='#ffffff',font_family='Manrope',size=16,
                          weight=ft.FontWeight.W_300)
filter3_name_text=ft.Text(value="Фильтр №3",color='#ffffff',font_family='Manrope',size=16,
                          weight=ft.FontWeight.W_300)
filter4_name_text=ft.Text(value="Фильтр №4",color='#ffffff',font_family='Manrope',size=16,
                          weight=ft.FontWeight.W_300)
filter5_name_text=ft.Text(value="Фильтр №5",color='#ffffff',font_family='Manrope',size=16,
                          weight=ft.FontWeight.W_300)

filter_qu1_cont=ft.Container(content=filter1_qu_text,bgcolor='#00A5FF',height=26,width=95,
                            alignment=ft.alignment.center,border_radius=5)
filter_qu2_cont=ft.Container(content=filter2_qu_text,bgcolor='#00A5FF',height=26,width=95,
                            alignment=ft.alignment.center,border_radius=5)
filter_qu3_cont=ft.Container(content=filter3_qu_text,bgcolor='#C5671F',height=26,width=95,
                            alignment=ft.alignment.center,border_radius=5)
filter_qu4_cont=ft.Container(content=filter4_qu_text,bgcolor='#AF0D0D',height=26,width=95,
                            alignment=ft.alignment.center,border_radius=5)
filter_qu5_cont=ft.Container(content=filter5_qu_text,bgcolor='#00A5FF',height=26,width=95,
                            alignment=ft.alignment.center,border_radius=5)

filter1_but_cont=ft.Row(controls=[filter1_name_text, filter_qu1_cont],spacing=140)
filter2_but_cont=ft.Row(controls=[filter2_name_text, filter_qu2_cont],spacing=140)
filter3_but_cont=ft.Row(controls=[filter3_name_text, filter_qu3_cont],spacing=140)
filter4_but_cont=ft.Row(controls=[filter4_name_text, filter_qu4_cont],spacing=140)
filter5_but_cont=ft.Row(controls=[filter5_name_text, filter_qu5_cont],spacing=140)


filter2_list_tile = ft.ElevatedButton(content=filter2_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341)

filter3_list_tile = ft.ElevatedButton(content=filter3_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341)

filter4_list_tile = ft.ElevatedButton(content=filter4_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341)

filter5_list_tile = ft.ElevatedButton(content=filter5_but_cont,bgcolor=ft.colors.with_opacity(0.5, '#3A4EB1'),
                                          style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                          height=46,width=341)
